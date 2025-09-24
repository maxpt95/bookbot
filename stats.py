from typing import TypedDict


class CharactersCount(TypedDict):
    char: str
    count: int


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


def sort_characters_count(
    characters_count: dict[str, int],
) -> list[CharactersCount]:
    """Sort character count from highest to lowest."""
    char_count_list = [
        CharactersCount(char=char, count=count)
        for char, count in characters_count.items()
    ]
    char_count_list.sort(reverse=True, key=lambda items: items["count"])

    return char_count_list
