def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    return file_contents
file_contents=main()
print(file_contents)
