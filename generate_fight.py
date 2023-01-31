import argparse
import unmatched

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--ban", nargs="+", help="Space-separated list of banned heroes. If a hero has a space in their name, preface that space with a '\\' on the command line.")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    banned_heroes = args.ban

    hero1, hero2, arena = unmatched.generate_fight(banned_heroes)
    print(f"{hero1} vs. {hero2} on {arena}")