import requests
import random
import time
import os

def init():
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    word = random.choice(WORDS)
    return word

def draw():
    if attempt < 6: head = chr(212)
    else : head = " "

    if attempt < 5: body = "|"
    else : body = " "
    
    if attempt < 4: left_hand = chr(92)
    else: left_hand = " "

    if attempt < 3: right_hand = "/"
    else: right_hand = " "

    if attempt < 2: left_leg = "/"
    else: left_leg = " "

    if attempt < 1: right_leg = chr(92)
    else: right_leg = " "

    print("   ________________")
    print("   | /            |")
    print("   |/             |")
    print("   |            ", left_hand + head + right_hand)
    print("   |             ",  body )
    print("   |            ", left_leg, right_leg)
    print("   |")
    print("   |")
    print("___|________")

word = init()
print(word)
for x in word:
    print("- ", end = "")
print()   
#attempt = 1
for attempt in range(6, -1, -1):
    os.system("cls")
    draw()
    time.sleep(1)
