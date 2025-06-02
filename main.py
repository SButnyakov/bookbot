import sys
from stats import get_num_words, get_num_symbols, get_chars_sorted_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    print(sys.argv)
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    chars_dict = get_chars_sorted_dict(get_num_symbols(text))   
    for char in chars_dict:
        symbol = char["char"]
        num = char["num"]
        if symbol.isalpha():
            print(f"{symbol}: {num}")
    print("============= END ===============")

main()
