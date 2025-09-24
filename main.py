from stats import (
    get_book_word_count,
    get_characters_count,
    sort_characters_count,
    CharactersCount,
)
import sys


def print_sorted_char_count(chars_count: list[CharactersCount]) -> None:
    for char_count in chars_count:
        if char_count["char"].isalpha():
            print(f"{char_count['char']}: {char_count['count']}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    word_count = get_book_word_count(book_text)
    char_count = get_characters_count(book_text)
    sorted_chars_count = sort_characters_count(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print_sorted_char_count(sorted_chars_count)
    print("============= END ===============")


def get_book_text(file_path: str) -> str:
    with open(file_path) as book:
        return book.read()


main()
