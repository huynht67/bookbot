from stats import count_words, count_characters

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

    num_words = count_words(text)
    print(f"Found {num_words} total words")

    char_counts = count_characters(text)
    print(char_counts)

main()
