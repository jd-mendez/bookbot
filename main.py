from stats import get_num_words, count_letters

def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    num_words = get_num_words(book)
    letters = get_chars_dict(book)

def get_book_text(book_path):
    with open(path) as f:
        return f.read()
    
main()