#!/usr/bin/env python
# -*- coding: utf-8 -*-
# zheng-ji.info

import argparse
from worker.snifer import Snifer


def get_opt():
    display = '''
     _____   _____    _____  __    __ __    __       _____   __   _   _   _____   _____   _____   _____   
     |  _  \ |  _  \  /  _  \ \ \  / / \ \  / /      /  ___/ |  \ | | | | |  ___| |  ___| | ____| |  _  \  
     | |_| | | |_| |  | | | |  \ \/ /   \ \/ /       | |___  |   \| | | | | |__   | |__   | |__   | |_| |  
     |  ___/ |  _  /  | | | |   }  {     \  /        \___  \ | |\   | | | |  __|  |  __|  |  __|  |  _  /  
     | |     | | \ \  | |_| |  / /\ \    / /          ___| | | | \  | | | | |     | |     | |___  | | \ \  
     |_|     |_|  \_\ \_____/ /_/  \_\  /_/          /_____/ |_|  \_| |_| |_|     |_|     |_____| |_|  \_\ 
    '''
    print display
    parser = argparse.ArgumentParser()
    parser.add_argument('--start_ip', type=str, nargs='?', default="")
    parser.add_argument('--end_ip', type=str, nargs='?', default="")
    parser.add_argument('--process_num', type=int, nargs='?', default="")
    parser.add_argument('--thread_num', type=int, nargs='?', default="")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = get_opt()
    instance = Snifer(args.start_ip, args.end_ip, args.process_num, args.thread_num)
    instance.valid_proxys_with_multiprocess()
