from collections import Counter

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = char_count(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in document")
    print()

    print_char_counts(num_chars)

    print("--- End Report ---")

def char_count(string):
    low_str = string.lower()
    return Counter(low_str)

def print_char_counts(chars):
    sort_by_value = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
    for char in sort_by_value:
        if char.isalpha():
            print(f"The '{char}' character was found {chars[char]} times")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()