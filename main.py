def main():
    book_path = 'books/frankenstein.txt'
    text = book_text(book_path)
    num_words = count_words(text)
    num_characters_total = count_characters(text)
    num_characters = count_characters_total(text)
    print(f'Words: {num_words}')
    print(f'Total Characters: {num_characters_total}')
    print(f'Characters: {num_characters}')

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
main()