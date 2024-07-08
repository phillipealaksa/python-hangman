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