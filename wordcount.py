import argparse
from collections import Counter
import re


def count_text(path: str):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    lines = text.splitlines()
    words = re.findall(r"\w+", text.lower())
    return len(lines), len(words), len(text), Counter(words)


def main():
    parser = argparse.ArgumentParser(description="Simple word count")
    parser.add_argument("file", help="Path to text file")
    args = parser.parse_args()
    lines, words, chars, freq = count_text(args.file)
    print(f"Lines: {lines}\nWords: {words}\nChars: {chars}")
    print("Top 5 words:", freq.most_common(5))


if __name__ == "__main__":
    main()
