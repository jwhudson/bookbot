def num_of_words(string):
    return len(string.split())

def character_count(string):
    formatted_string = string.lower()

    output = {}

    for char in formatted_string:
        if char in output:
            output[char] += 1
        else:
            output[char] = 1
    return output

def sort_on(dict):
    return dict.keys()

def char_count_sorted(char_dictionary):
    keys = []

    for key, value in char_dictionary.items():
        if key.isalpha():
            keys.append((value, key))

    keys.sort(reverse=True, key=lambda x: x[0])    
    sorted_chars = []

    for key in keys:
        sorted_chars.append({key[0]: key[1]})
    
    return sorted_chars

    