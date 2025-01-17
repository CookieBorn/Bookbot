from itertools import count
def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    return file_contents
file_contents=main()
def wordcount():
    words=(file_contents.casefold()).split()
    number=len(words)
    return number, words
words=wordcount()
print(words)
def lettercount():
    v=file_contents.count("v")
    return v
letters=lettercount()
print(letters)
