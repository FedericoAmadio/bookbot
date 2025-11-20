from stats import word_counter
from stats import character_counter
from stats import dictionary_to_sorted_list
import sys

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    number = word_counter(text)
    characters = character_counter(text)
    character_list = dictionary_to_sorted_list(characters)
    print_report(book_path, number, character_list)
    
    
def print_report(book_path, number, character_list):
    print("============ BOOKBOT ============")
    print("Analyzing book found at", book_path, "...")
    print("----------- Word Count ----------")
    print("Found", number, "total words")
    print("--------- Character Count -------")
    for item in character_list:
        if not item["character"].isalpha():
            continue
        print (f"{item["character"]}: {item["num"]}")
    print ("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()