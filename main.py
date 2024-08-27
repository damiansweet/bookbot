def main():
    book = "./books/frankenstein.txt"
    book_contents = read_book(book)
def read_book(book):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

main()