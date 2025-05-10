from stats import *
import sys

def get_book_text(text):
    print(f"{num_of_words(text)} words found in the document")

def print_report(path, word_count, character_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for entry in character_count:
        for key, value in entry.items():
            print(f"{value}: {key}")

    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    with open(path) as f:
        text = f.read()
    char_count = character_count(text)

    chars = char_count_sorted(char_count)

    print_report(path, num_of_words(text), chars)

main()