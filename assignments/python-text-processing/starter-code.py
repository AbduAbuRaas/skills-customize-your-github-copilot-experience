#!/usr/bin/env python3
"""Starter scaffold for Python Text Processing assignment.

Features to implement or extend:
- Count lines, words and characters
- Show top-N most common words (ignore case, basic punctuation)
- Search for a term (case-insensitive) and list occurrences with line numbers
"""

import sys
import argparse
import re
from collections import Counter


def tokenize(text):
    # simple tokenizer: lowercase and split on non-word characters
    return [t for t in re.findall(r"\b\w+\b", text.lower())]


def analyze_file(path, top=10, search=None):
    lines = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error opening file: {e}")
        return

    text = "".join(lines)
    words = tokenize(text)

    print(f"Lines: {len(lines)}")
    print(f"Words: {len(words)}")
    print(f"Characters: {len(text)}")

    counter = Counter(words)
    print(f"Top {top} words:")
    for word, count in counter.most_common(top):
        print(f"{word}: {count}")

    if search:
        s = search.lower()
        occurrences = []
        for i, line in enumerate(lines, start=1):
            if re.search(rf"\b{re.escape(s)}\b", line, re.IGNORECASE):
                occurrences.append(i)
        print(f"\nSearch '{search}': found {len(occurrences)} occurrences on lines: {occurrences}")


def main():
    parser = argparse.ArgumentParser(description="Simple text processing starter")
    parser.add_argument("path", help="Path to text file")
    parser.add_argument("--top", type=int, default=10, help="Top N words to show")
    parser.add_argument("--search", help="Search term (case-insensitive)")

    args = parser.parse_args()
    analyze_file(args.path, top=args.top, search=args.search)


if __name__ == "__main__":
    main()
