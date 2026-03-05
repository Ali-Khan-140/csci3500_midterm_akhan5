from dataclasses import dataclass
from datetime import date
import argparse

@dataclass
class LostItem:
    sku: str
    expected: int
    actual: int

def check_missing(item: LostItem):
    missing = item.expected - item.actual
    if missing > 0:
        print(f"{item.sku} is missing {missing} items.")
    else:
        print(f"{item.sku} inventory is correct.")

def main():
    parser = argparse.ArgumentParser(description="Lost Item Tracker")
    parser.add_argument("--sku", required=True)
    parser.add_argument("--expected", type=int, required=True)
    parser.add_argument("--actual", type=int, required=True)

    args = parser.parse_args()

    item = LostItem(args.sku, args.expected, args.actual)
    check_missing(item)

if __name__ == "__main__":
    main()