import sys
from stats import count_words
from stats import count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        num_words = count_words(text)
        num_characters = count_characters(text)
    return(text)

def main():
    #filepath = 'books/frankenstein.txt'
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    num_characters = count_characters(book_text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    for character in num_characters:
        print(f"{character['name']}: {character['num']}")

main()