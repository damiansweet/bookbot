def main():
    book = "./books/frankenstein.txt"
    book_contents = read_book(book)
    word_count = count_words(book_contents)
    char_count = count_chars(book_contents)
    print(char_count)
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

main()