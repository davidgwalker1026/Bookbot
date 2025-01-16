with open("books/frankenstein.txt") as f:
    book = f.read()
    words = book.split()
    sum = len(book)
    print(sum)