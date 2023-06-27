import os

def create_dictionary():
    
    if not os.path.isfile('dictionary.txt'):
        with open('dictionary.txt', 'w') as f:
            pass

def add_word(word, meaning):
    
    with open('dictionary.txt', 'a') as f:
        f.write(f'{word}: {meaning}\n')

def search_word(word):
    
    with open('dictionary.txt', 'r') as f:
        for line in f:
            if line.startswith(word + ':'):
                return line.split(': ')[1].strip()

def remove_word(word):
    
    with open('dictionary.txt', 'r') as f:
        lines = f.readlines()
    with open('dictionary.txt', 'w') as f:
        for line in lines:
            if not line.startswith(word + ':'):
                f.write(line)

def main():
    
    create_dictionary()
    while True:
        action = input('Enter "add" to add a word, "search" to search for a word, "remove" to remove a word, or "exit" to quit: ')
        if action == 'add':
            word = input('Enter a word: ')
            meaning = input('Enter the meaning: ')
            add_word(word, meaning)
            print('Word added successfully.')
        elif action == 'search':
            word = input('Enter a word: ')
            meaning = search_word(word)
            if meaning:
                print(meaning)
            else:
                print('Word not found.')
        elif action == 'remove':
            word = input('Enter a word: ')
            remove_word(word)
            print('Word removed successfully.')
        elif action == 'exit':
            break
        else:
            print('Invalid input. Please try again.')

if __name__ == '__main__':
    main()
