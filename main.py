import sys, os
import requests
import threading
import time
import random

def load_screen():
    i = 0
    while not event.is_set():
        print("Loading" + "." * ((i % 3) + 1))
        time.sleep(0.5)
        os.system('cls')
        i += 1

def process_data(data):
    wordlengths = {}
    for word in data:
        length = len(word)
        if length in wordlengths:
            wordlengths[length].append(word)
        else:
            wordlengths[length] = [word]
    return wordlengths

def get_word(wordsbylength):
    length = input("Enter the length of the word you want to guess: ")
    while not length.isdigit() or int(length) not in wordsbylength:
        if not length.isdigit():
            input("Invalid input")
        elif int(length) not in wordsbylength:
            input("No words of this length")
        os.system('cls')
        length = input("Enter the length of the word you want to guess: ")
    length = int(length)
    word = random.choice(wordsbylength[length])
    word = word.upper()
    return word

def get_all_indices(word, char):
    indices = []
    for i in range(len(word)):
        if word[i] == char:
            indices.append(i)
    return indices

def game(word):
    os.system('cls')
    lives = 10
    currentlist = ["_"] * len(word)
    currentstring = ''.join(currentlist)
    guessed = []

    while lives > 0 and currentstring != word:
        print("Lives: " + str(lives))
        print("Guessed: " + str(guessed))
        print("Current: " + currentstring)
        char = input("Enter a character: ")
        char = char.upper()
        if len(char) != 1 or not char.isalpha():
            input("Invalid input")
            os.system('cls')
            continue
        if char in guessed:
            input("You have already guessed this character")
            os.system('cls')
            continue
        guessed.append(char)
        if char in word:
            indicies = get_all_indices(word, char)
            for index in indicies:
                currentlist[index] = char
            currentstring = ''.join(currentlist)
            input("Correct guess")
            os.system('cls')
        else:
            lives -= 1
            input("Incorrect guess")
            os.system('cls')
    if lives == 0:
        input("You lost! The word was: " + word)
    else:
        input("You won! The word was: " + word)

def main(wordsbylength):
    os.system('cls')
    print("1. Play Game")
    print("2. Exit")
    choice = input("Enter your choice: ")
    while not (choice == "1" or choice == "2"):
        input("Invalid choice")
        os.system('cls')
        print("1. Play Game")
        print("2. Exit")
        choice = input("Enter your choice: ")
    if choice == "1":
        
        main(wordsbylength)
    else:
        sys.exit()

if __name__ == '__main__':
    os.system('cls')

    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json"

    event = threading.Event()
    t = threading.Thread(target=load_screen)
    t.start()

    response = requests.get(url) 

    event.set()
    t.join()
    
    if response.status_code == 200:
        data = response.json()
        wordsbylength = process_data(data)
        main(wordsbylength)
    else:
        print("Failed to fetch data")
        sys.exit()