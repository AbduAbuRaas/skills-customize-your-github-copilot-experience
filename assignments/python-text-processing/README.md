# 📘 Assignment: Python Text Processing

## 🎯 Objective

Practice working with strings, file I/O, and basic text processing in Python. Students will write programs that read text files, analyze and transform text, and produce useful summaries (word counts, most-common words, simple search/replace).

## 📝 Tasks

### 🛠️ Implement core text-processing utilities

#### Description
Create a Python program that loads a text file and implements a small set of text-processing features: counting lines/words/characters, finding the most common words, and performing a simple search or replace.

#### Requirements
Completed program should:

- Accept a path to a text file (via command-line argument or interactive input) and validate the file exists and is readable.
- Print the total number of lines, words, and characters in the file.
- Produce a frequency list of the top N most common words (ignore case and basic punctuation). N should be configurable (default 10).
- Support a case-insensitive search for a word and show how many occurrences were found and the line numbers where they occur.

### 🛠️ Add polish and optional features

#### Description
Improve usability and robustness with input validation, small transformations, and optional features.

#### Requirements
Students should implement one or more of the following enhancements:

- Provide a `--replace` option to replace a given word with another and optionally write the result to a new file.
- Allow the program to ignore a small list of stopwords when counting common words.
- Add a simple command-line interface using `argparse` with flags for `--top`, `--search`, and `--replace`.
- Load the stopword list from an external file.

## Example usage

```bash
python starter-code.py sample.txt --top 5

# Output (example):
# Lines: 120
# Words: 1,013
# Characters: 6,742
# Top 5 words: the (73), and (58), to (47), of (44), a (39)
# Search 'python': found 7 occurrences on lines: 4, 10, 47, 59, 63, 88, 104
```

## Starter files

Included: `starter-code.py` — a minimal scaffold that reads a file and implements counting and top-N word frequency.

## Learning outcomes

- Read and validate files using Python file I/O.
- Use string methods and regular expressions for simple text cleaning and tokenization.
- Use collections (e.g., Counter) to count and rank items.
- Build a small CLI and practice defensive input handling.
