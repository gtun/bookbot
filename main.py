import sys
from stats import count_words, characters_dict, chars_dict_to_sorted_list


def get_book_text(filepath:str) -> str:
    contents: str = ""

    with open(filepath) as f:
            contents = f.read()

    return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath: str = sys.argv[1]

#    print(get_book_text(pathToFrankenstein))
    book_text:str = get_book_text(filepath)

    num_words: int = count_words(book_text)
    print(f"Found {num_words} total words")

    count_per_character: dict[str, int] = characters_dict(book_text)
#    print(count_per_character)

    sorted_count_per_character: list[tuple[str, int]] = chars_dict_to_sorted_list(count_per_character)
#    print(sorted_count_per_character)

    print_report(filepath, num_words, sorted_count_per_character)

def print_report(filepath: str, word_count: int, sorted_characters: list[tuple[str, int]]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for character in sorted_characters:
        if character[0].isalpha():
            print(f"{character[0]}: {character[1]}")

    print("============= END ===============")

main()