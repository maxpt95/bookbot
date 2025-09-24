from stats import get_book_word_count


def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = get_book_word_count(book_text)
    print(f"Found {word_count} total words")


def get_book_text(file_path: str) -> str:
    with open(file_path) as book:
        return book.read()


main()
