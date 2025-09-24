from stats import get_book_word_count, get_characters_count


def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = get_book_word_count(book_text)
    print(f"Found {word_count} total words")
    print(get_characters_count(book_text))


def get_book_text(file_path: str) -> str:
    with open(file_path) as book:
        return book.read()


main()
