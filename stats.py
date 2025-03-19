

def get_num_words():
    with open("books/frankenstein.txt") as file:
        text = file.read()
    words = text.split()
    word_count = len(words)
    print(word_count, "words found in the document")
get_num_words()

def count_letters():
    with open("books/frankenstein.txt") as file:
        text = file.read() 
    letters = text.lower()
    letter_count = {}
    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    print(letter_count)
count_letters()
     

    
        
   