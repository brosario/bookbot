'''
Brian Rosario
Bookbot

This program asks the user for the file path of a file and 
    -counts the amount of words found in the document
    -counts how often each letter of the alphabet is found and prints the results
        in descending order.
'''

def dict_items_to_list(char_dict):
    '''
    takes the dictionary of characters and their occurence value
    splits the dictionary into two lists - one of keys, one of values
    '''
    char_dict_keys = list(char_dict.keys())
    char_dict_values = list(char_dict.values())

    return char_dict_keys, char_dict_values

def alpha_count(char_count):
    '''
    takes the two lists resulting from the split character dictionary and
    iterates through to check for alphabet characters.
    creates new dictionary of sorted results in descending order.
    '''
    char_dict_keys, char_dict_values = dict_items_to_list(char_count)
    alpha_count_dict = {}
    
    for i, element in enumerate(char_dict_keys):
        if element.isalpha():
            alpha_count_dict[element] = char_dict_values[i]

    sorted_alpha_count = dict(sorted(alpha_count_dict.items(), key=lambda x:x[1], reverse=True))

    return sorted_alpha_count

def character_count(file):
    '''
    takes the file and creates a dictionary of the frequency of each character
    '''
    char_dict = {}
    lowered_file = file.lower()

    for c in lowered_file:
        if c not in char_dict:
            char_dict[c] = 1
        else:
            char_dict[c] = char_dict[c] + 1

    return char_dict

def word_count(file):
    '''
    counts the number of words in the file
    '''
    count = len(file.split())
    return count

def file_report(file_path, file_contents):
    '''
    prints to console
        -begin report
        -word count of document
        -frequency of each alphabet character in file
        -end report
    '''
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count(file_contents)} words found in the document")
    print()
    char_count = character_count(file_contents)
    alpha_dict = alpha_count(char_count)
    for key,value in alpha_dict.items():
        print(f"The '{key}' character was found {value} times.")
    print("--- End report ---")

def main():
    file_path = input("Please enter file path: ")
    with open(file_path) as f:
        file_contents = f.read()
        file_report(file_path, file_contents)

main()
