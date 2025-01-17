from itertools import count
def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    return file_contents
file_contents=main()
def wordcount():
    words=file_contents.split()
    number=len(words)
    return number
words=wordcount()
print(words)
