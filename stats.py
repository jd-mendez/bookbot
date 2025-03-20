
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = text.lower()
    character_count = {}
    for c in characters:
        if c in character_count:
            character_count[c] += 1
        else:
            character_count[c] = 1
    return character_count

def sort_on(d):
    return d["num"]

def character_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num":num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list