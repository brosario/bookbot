
def word_count(file):
    count = len(file.split())
    return count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        print(word_count(file_contents))
main()
