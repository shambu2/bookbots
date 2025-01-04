def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    # print(num_words)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    objects_of_chars = (get_char_num(text))
    
    
    iterating(objects_of_chars)
def get_num_words(text):
    words = text.split()
    return len(words)

def iterating(key_value):
    my_dict = key_value
    # xyz = my_dict.key()
    filtered_dict = {key: value for key, value in my_dict.items() if key.isalpha()}
    sorted_dict = dict(sorted(filtered_dict.items(),key=lambda item: item[1],reverse=True))
    for key,value in sorted_dict.items():
        
        print(f"the '{key}' character was found {value} times")
   
def get_char_num(text):
    chars ={}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] +=1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
