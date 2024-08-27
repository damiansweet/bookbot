def main():
    book = "./books/frankenstein.txt"
    book_contents = read_book(book)
    word_count = count_words(book_contents)
def read_book(book):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents
def count_words(book_str):
    words = book_str.split()
    return len(words)

main()