#!/usr/bin/env python3

import argparse
import unmatched

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--count", nargs='?', help="How many fights to show.")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    if args.count:
        unmatched.show_fights(args.count)
    else:
        unmatched.show_fights()