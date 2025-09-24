def main():
    print(get_book_text("books/frankenstein.txt"))


def get_book_text(file_path: str) -> str:
    with open(file_path) as book:
        return book.read()


main()
