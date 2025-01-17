def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    return file_contents
file_contents=main()
def wordcount():
    words=(file_contents.casefold()).split()
    return words
words=wordcount()
print(words)
number=len(words)
print(number)
letters={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
alphabet={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

def lettercount():
    for word in words:
        for letter in letters:
            alphabet[letter]=alphabet[letter]+word.count(letter)
    return alphabet
letter_count=lettercount()
print(letter_count)

def report():
    for letter in letters:
        a=f"There are {letter_count[letter]} occurrences of {letter}"
        print(a)
    return
reports=report()
print(reports)
