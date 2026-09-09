def count_words(book_text:str) -> int:
    return len(book_text.split())

def characters_dict(book_text:str) -> dict[str, int]:
    lowercased_text: str = book_text.lower()
    book_characters: dict[str, int] = {}

    for character in lowercased_text:
        if character in book_characters:
            book_characters[character] += 1
        else:
            book_characters[character] = 1

    return book_characters

def sort_on(character_count: tuple[str, int]) -> int:
    return character_count[1]

def chars_dict_to_sorted_list(chars_dict: dict[str, int]) -> list[tuple[str, int]]:
    new_list:list[tuple[str, int]] = []

    for char in chars_dict:
        new_list.append((char, chars_dict[char]))
    
    sort_list:list[tuple[str, int]] = sorted(new_list, reverse=True, key=sort_on)

    return sort_list

