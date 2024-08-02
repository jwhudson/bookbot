def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    number_of_words = word_count(book_text)
    number_of_characters = character_count(book_text)
    ordered_characters = order_characters(number_of_characters)

    print_report(number_of_words, ordered_characters)
        
def word_count(input_string):
    words = input_string.split()

    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def character_count(text):
    characters = {}
    for letter in text:
        character = letter.lower()

        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    
    return characters

def order_characters(characters):
    output_list = list()
    for char in characters:
        if char.isalpha():
            output_list.append({ "letter": char, "count": characters[char]})
    
    output_list.sort(reverse=True, key=sort_on)
    return output_list

def sort_on(dict):
    return dict["count"]

def print_report(word_count, ordered_characters):
    print("Begin report of Frankenstein.txt")
    print(f"There are {word_count} words in this document.")
    print("")
    for entry in ordered_characters:
        print(f"The '{entry['letter']}' character appeared {entry['count']} times.")
    print("--------End of report--------")


main()
