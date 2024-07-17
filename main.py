
def character_count(file):
    char_dict = {}

    lowered_file = file.lower()
    for c in lowered_file:
        if c not in char_dict:
            char_dict[c] = 1
        else:
            char_dict[c] = char_dict[c] + 1

    return char_dict

def word_count(file):
    count = len(file.split())
    return count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        print(word_count(file_contents))
        print(character_count(file_contents))

main()
