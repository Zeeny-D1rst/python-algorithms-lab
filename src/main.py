"""Command-line interface for the algorithms lab."""
import argparse
from .algorithms import SORTS, binary_search, linear_search


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Sorting and searching algorithms demo")
    commands = parser.add_subparsers(dest="command", required=True)
    sort_parser = commands.add_parser("sort", help="sort a sequence of integers")
    sort_parser.add_argument("--algorithm", choices=sorted(SORTS), default="merge")
    sort_parser.add_argument("--numbers", nargs="*", type=int, default=[])
    search_parser = commands.add_parser("search", help="search for an integer")
    search_parser.add_argument("--algorithm", choices=["linear", "binary"], default="binary")
    search_parser.add_argument("--target", type=int, required=True)
    search_parser.add_argument("--numbers", nargs="*", type=int, default=[])
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.command == "sort":
        print(SORTS[args.algorithm](args.numbers))
        return
    if args.algorithm == "binary" and args.numbers != sorted(args.numbers):
        raise SystemExit("Binary search requires --numbers in ascending order.")
    search = binary_search if args.algorithm == "binary" else linear_search
    index = search(args.numbers, args.target)
    print(f"Found at index {index}" if index >= 0 else "Value not found")


if __name__ == "__main__":
    main()
