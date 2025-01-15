
# Word Finder

## Description
This program searches for words in a given file based on specific filtering criteria. It allows users to filter words by length, excluded letters, included letters with specific indices, and included letters with excluded indices.

## Features
- Filter words based on length.
- Exclude words containing specific letters.
- Include words with specific letters at specific positions.
- Exclude words with specific letters at certain positions.

## Usage
Run the program from the command line with the following arguments:

### Required Arguments:
1. `file` - Path to the file containing a list of words.
2. `length` - Desired length of the words.

### Optional Arguments:
- `--not_contain` or `-nc` - Letters that should not be present in the word.
- `--contain_displace` or `-cd` - Letters that must be present but cannot be at specific indices. Format: `<char><i>` (e.g., `a0` for 'a' cannot be at index 0).
- `--contain` or `-c` - Letters that must be present at specific indices. Format: `<char><i>` (e.g., `b2` for 'b' at index 2).

### Example Command:
```bash
python script.py .txt 5 -nc xyz -cd 'a0 b1' -c 'c2 d3'
```

## Prerequisites
- Python 3.x
- A text file containing the list of words, one word per line.

## How It Works
1. Reads words from the provided file.
2. Filters words based on the specified criteria.
3. Outputs the filtered list of words.
