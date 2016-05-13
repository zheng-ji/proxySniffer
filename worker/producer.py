#!/usr/bin/env python
# -*- coding: utf-8 -*-
# zheng-ji.info


class Producer():
    """
    IP 产生类
    """

    def ip2num(self, i):
        ip = [int(x) for x in i.split('.')]
        return ip[0] << 24 | ip[1] << 16 | ip[2] << 8 | ip[3]

    def num2ip(self, n):
        return '%s.%s.%s.%s' % (
            (n & 0xff000000) >> 24,
            (n & 0x00ff0000) >> 16,
            (n & 0x0000ff00) >> 8,
            n & 0x000000ff)

    def ports(self):
        """
        要扫描的端口,
        本来是计划前部端口扫描， 但太慢了
        于是选举了一些较常见的
        """

        #return [8123, 8118, 3128, 80, 8090, 8080, 9999, 8888, 8001, 8088, 9080, 82, 18186, 8585, 9000, 9797]
        return [80, 81, 8080, 9999]

    def gen(self, s, e):
        return [self.num2ip(n) for n in range(self.ip2num(s), self.ip2num(e)+1) if n & 0xff]

    def chunks(self, arr, n):
        """
        按照步长, 将 IP 数组分块, 供多个 process 操作
        """
        return [arr[i:i+n] for i in range(0, len(arr), n)]
