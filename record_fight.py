#!/usr/bin/env python3

import argparse
import unmatched

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--winner", nargs=1, help="The fight's winner.")
    parser.add_argument("-l", "--loser",  nargs=1, help="The fight's loser.")
    parser.add_argument("-a", "--arena",  nargs=1, help="The fight's arena.")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    unmatched.record_fight(args.winner[0], args.loser[0], args.arena[0])
    print(f"{args.winner[0]} killed {args.loser[0]} in {args.arena[0]}")