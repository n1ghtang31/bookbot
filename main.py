def main():
    book_path = 'books/frankenstein.txt'
    text = book_text(book_path)
    num_words = count_words(text)
    num_characters = count_characters(text)
    #num_characters_total = count_characters_total(text)
    num_characters_sorted = character_sort(num_characters)
    print_report(num_words, num_characters_sorted, book_path)

    

def book_text(path):
    with open(path) as f:
        file_contents = f.read()
        #print(file_contents)
        return file_contents

def count_words(file_contents):
        words = file_contents.split()
        return len(words)

def count_characters_total(file_contents):
    return len(file_contents)

def count_characters(file_contents):
    text = file_contents.lower()
    count = {}
    for char in text:
        if char.isalpha():
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

    return count


def character_sort(dict):
    sorted_key = sorted(dict.keys())
    sorted_dict = {key: dict[key] for key in sorted_key}
    return sorted_dict





def print_report(words, characters, path):
    print(f"--- Begin report of {path} ---")   
    print(f"{words} words found in the document") 
    for char, count in characters.items():
        print(f"The '{char}' character was found {count} times")

    print(f"--- End report ---")


main()