def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    number_of_words = word_count(book_text)
        
    print(number_of_words)

        
def word_count(input_string):
    words = input_string.split()

    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()

