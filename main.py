from stats import count_words

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

    num_words = count_words(text)
    print(f"Found {num_words} total words")

main()
