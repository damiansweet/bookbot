def main():
    book = "./books/frankenstein.txt"
    book_contents = read_book(book)
    word_count = count_words(book_contents)
    char_count = count_chars(book_contents)
    sorted_char_count = sort_dict(char_count)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("\n")
    for char in sorted_char_count:
        if char["char"].isalpha():
            print(f"The '{char['char']}' character was found {char['num']} times")
    print("--- End report ---")

def read_book(book):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count_words(book_str):
    words = book_str.split()
    return len(words)

def count_chars(book):
    char_count = {}
    for b in book:
        b = b.lower()
        if b in char_count:
            char_count[b] += 1
        else:
            char_count[b] = 1
    return char_count

def sort_on(d):
    return d["num"]

def sort_dict(char_dict):
    sorted_chars = [{"char": k, "num": v} for k, v in char_dict.items()]
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars

main()