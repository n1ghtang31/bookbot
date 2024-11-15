def main():
    book_path = 'books/frankenstein.txt'
    text = book_text(book_path)
    num_words = count_words(text)
    print(num_words)


def book_text(path):
    with open(path) as f:
        file_contents = f.read()
        #print(file_contents)
        return file_contents

def count_words(file_contents):
        words = file_contents.split()
        return len(words)

main()