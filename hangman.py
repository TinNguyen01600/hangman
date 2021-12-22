import requests
import random
import time
import os

def init():
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    word = random.choice(WORDS)         #get a random word from the list
    word = word.decode('utf-8')         #decode word from byte object to string
    return word

def draw(attempt):
    if attempt < 6: head = chr(212)     #212 is the ASCII code for symbol Ô 
    else : head = " "                   #if the attempt = 6, print nothing

    if attempt < 5: body = "|"
    else : body = " "
    
    if attempt < 4: left_hand = chr(92) #92 is the ASCII code for symbol \
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
    print("   |")
    print("___|________")
    print()

def play(attempt, word, temp):
    while (attempt > 0):
        draw(attempt)
        count = 0
        print ("You have %d attempts left" % (attempt))
        c = input("Your guess: ")
        for x in range(0, len(word)):
            if c == word[x]:
                count += 1
                temp[x] = c
        if count > 0: 
            print("Well done!!! %d letter(s) '%c'" % (count, c))
        else:
            print("Oh no!!! There is no letter '%c'." % (c))
            attempt -= 1
        time.sleep(1.7)
        os.system("cls")
        string = " ".join(temp)
        print ("The word has %d letters" % (len(word)))
        print(string)
    os.system("cls")
    draw(attempt)
    print("YOU LOST :((((")
    print("The word is %s." % word)
    time.sleep(2)
    os.system("cls")
    loop()
   
def new_game():
    word = init()

    print(word)

    attempt = 6
    print ("The word has %d letters" % (len(word)))
    temp = list(word)
    for x in range(0, len(temp)):
        temp[x] = "-"
    string = " ".join(temp)
    print(string)
    play(attempt, word, temp)

def loop():
    print("HANG-MAN")
    print("N - New game")
    print("E - Exit")
    n = input("")
    if (n == "N" or n == "n"):
        os.system("cls")
        new_game()
    elif (n == "E" or n == "e"):
        print("Bye bye @(^_^)@ ")
        time.sleep(1)
        os.system("cls")
        exit(0)
    else:
        print("Invalide option!!! Please try again.")
        time.sleep(1.7)
        os.system("cls")
        loop()

os.system("cls")
loop()  

