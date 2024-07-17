

def dict_items_to_list(char_dict):
    char_dict_keys = list(char_dict.keys())
    char_dict_values = list(char_dict.values())

    return char_dict_keys, char_dict_values

def file_report(char_count):
    char_dict_keys, char_dict_values = dict_items_to_list(char_count)
    alpha_count_dict = {}
    '''
    for i in range(len(char_dict_keys)):
        if char_dict_keys[i].isalpha():
            alpha_count_dict[char_dict_keys[i]] = char_dict_values[i]
    '''
    for i, element in enumerate(char_dict_keys):
        if element.isalpha():
            alpha_count_dict[element] = char_dict_values[i]

    return alpha_count_dict


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
        #print(file_contents)
        #print(word_count(file_contents))
        char_count = character_count(file_contents)
        print(file_report(char_count))



main()
