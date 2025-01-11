def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    freq_letters = count_letters(text)
    chars_sorted_list = sorted_letters(freq_letters)
    
    print(f"--- Begin report of {book_path} ---")
    print (f"{num_words} words found in the document")
    print ()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"the '{item['char']} character was found {item['num']} times")
    print("--- End report ---")

def sort_on(d):
    return d["char"]

def sorted_letters(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=False, key=sort_on)
    return sorted_list    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(text):
    full_text = text.lower()
    frequency = {}
    for i in full_text:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency

main()