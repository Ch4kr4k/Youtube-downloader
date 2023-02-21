#!/usr/bin/env python
# import os

import sys
import argparse
# import getopt
from download import driver


def main(args):
    if args.r == '2160p':
        driver(args.l, args.r)
    elif args.r == '1440p':
        driver(args.l, args.r)
    elif args.r == '1080p':
        driver(args.l, args.r)
    else:
        print("try lower resolutions")
   # opts, args = getopt.getopt(sys.argv[1:], "l:r:", ["link", "resolution"])
   # for opt, args in opts:
   #     if opt == '-l':
   #         link = args
   #     if opt == '-r':
   #         resolution = args
   # print(f"{link} and {resolution}")

    #  driver(link, resolution)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='youtube downloader')
    parser.add_argument('-l',help="link of youtube video", required = True)
    parser.add_argument('-r',default='1080p',help="resolution", required = True)
    args = parser.parse_args()
    main(args)
