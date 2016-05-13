#!/usr/bin/env python
# -*- coding: utf-8 -*-
# zheng-ji.info

import requests
from producer import Producer
import gevent.monkey
from multiprocessing import Process

gevent.monkey.patch_socket()

pd = Producer()
CHECK_LEN = 2695


class Snifer():
    """
    用 Gevent + MultiProcess 加速扫描代理
    """

    def __init__(self, startIp, endIp, processNum, threadNum):
        self.startIp = startIp
        self.endIp = endIp
        self.threadNum = threadNum
        self.processNum = processNum

    def valid_proxy(self, proxy_url):
        try:
            proxies = {"http": proxy_url}
            r = requests.get(
                "http://img0.bdstatic.com/img/image/logo_cacece1e9a.png",
                proxies=proxies,
                timeout=4
            )
            is_valid = False
            if len(r.text) == CHECK_LEN:
                is_valid = True
            return is_valid
        except requests.exceptions.ProxyError:
            return False
        except Exception:
            return False

    def valid_proxy_job(self, queue):
        while len(queue) > 0:
            host = queue.pop()
            for port in pd.ports():
                proxy = "http://%s:%s" % (host, port)
                is_valid = self.valid_proxy(proxy)
                if is_valid:
                    print "good %s" % proxy

    def valid_proxys_with_gevent(self, proxy_list):
        """
        在每一个进程里，使用 Gevent
        """

        threads = []
        for i in range(int(self.threadNum)):
            threads.append(gevent.spawn(self.valid_proxy_job, proxy_list))
        gevent.joinall(threads)

    def valid_proxys_with_multiprocess(self):
        """
        将 IP 按照进程数分块，分别交给 multiprocess 处理
        """

        proxy_list = pd.gen(self.startIp, self.endIp)
        step = len(proxy_list) / self.processNum
        chunk_proxy_list = pd.chunks(proxy_list, step)

        process = []
        for item in chunk_proxy_list:
            p = Process(target=self.valid_proxys_with_gevent, args=(item, ))
            p.start()
            process.append(p)

        for item in process:
            p.join()
