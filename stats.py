def get_book_word_count(book_text: str) -> int:
    return len(book_text.split())


def get_characters_count(book_text: str) -> dict[str, int]:
    char_count = {}
    for c in book_text.lower():
        if char_count.get(c):
            char_count[c] += 1
        else:
            char_count[c] = 1

    return char_count
