# Word Finder Program

This program helps you search for words in a given word list file based on specified criteria such as length, excluded letters, and constraints on letter positions.

## Features

- **Filter by word length:** Search for words of a specific length.
- **Exclude letters:** Eliminate words containing specific letters.
- **Include letters with constraints:** Find words that must contain specific letters but not at certain indices.
- **Exact letter placement:** Find words with specific letters at exact indices.

## Usage

### Requirements

- Python 3.6 or later

### Installation

1. Clone this repository or copy the program file to your local machine.
2. Ensure you have a word list file (e.g., `words.txt`) formatted as one word per line.

### Command-Line Interface

Run the program using the following command:

```bash
python word_finder.py <file> <length> [--not_contain <letters>] [--contain_displace <char><index>] [--contain <char><index>]
