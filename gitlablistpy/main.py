import sys
import argparse
from . import projects


def main():
    parser = argparse.ArgumentParser(prog="gitlablistpy")
    subparsers = parser.add_subparsers()

    projects.get_parser(subparsers)

    if len(sys.argv) < 2:
        parser.print_help()
        exit(1)
    else:
        args = parser.parse_args()
        args.func(args)


if __name__ == "__main__":
    main()
