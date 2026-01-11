import sys

from stats import count_words, count_characters, get_sorted_char_counts

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    #book_path = "books/frankenstein.txt"

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    print(text)

    num_words = count_words(text)
    print(f"Found {num_words} total words")

    char_counts = count_characters(text)
    print(char_counts)

    sorted_chars = get_sorted_char_counts(char_counts)

    print("============= BOOKBOT =============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    
    print("============= END =================")

main()
