import sys, os
import requests
import threading
import time

def load_screen():
    i = 0
    while not event.is_set():
        print("Loading" + "." * ((i % 3) + 1))
        time.sleep(0.5)
        os.system('cls')
        i += 1


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
        
    else:
        print("Failed to fetch data")
        sys.exit()