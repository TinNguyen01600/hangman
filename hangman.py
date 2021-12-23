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
    count_letter = 0            #this variable count_letter counts how many letter you guessed correctly
    tried = []                  #this list stores the letters you have entered
    while (attempt > 0 and count_letter != len(word)):
        draw(attempt)
        count = 0
        #str_tried = " ".join(tried)

        print ("You have %d attempts left    |    Tried letters: %s" % (attempt, tried))
        c = input("Your guess: ")       #your guess letter is stored in this variable c
        
   
#--------------------------------------------------------------------------------------------------
        while True:                                 #This part of code checks if the letter you entered
            count_repl_letter = 0                   #is already in the 'tried' list
            for x in tried:
                if c == x:                          #if you enter a letter already exists in 'list'
                    count_repl_letter += 1          #the variable count_repl_letter increases by 1
            if (len(c) > 1):
                print("!!! Invalid input !!!")
                c = input("Please try again: ")
            elif count_repl_letter > 0:
                print("!!! You have already entered this letter !!!")
                c = input("Please try another one: ")          #and you have to try another letter
            else:
                break                               #else (the letter you entered is not in 'list') you can exit the loop
#-------------------------------------------------------------------------------------------------
        tried.append(c)                 #add your guess letter to list 'tried'

        for x in range(0, len(word)):
            if c == word[x]:            #compare c to every letter in word
                count_letter += 1
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

    if (attempt == 0):              #you have no more attempt left
        print("YOU LOST :((((")
    elif (count_letter == len(word)):   #you already correctly guessed all the letters of the word
        print("Congratulations!!! YOU WON")
    draw(attempt)
    print("The word is %s." % word)
    time.sleep(3)                   #delay for 3 seconds before clearing the screen
    os.system("cls")                #clear the cmd screen
    loop()                          #come back to main menu
   
def new_game():
    word = init()
    attempt = 6                     #the player has initially 6 tries
    print ("The word has %d letters" % (len(word)))
    temp = list(word)               #this 'temp' variable is the list of letter of word
    for x in range(0, len(temp)):
        temp[x] = "-"               #change all the letter into '-' in 'temp'
                                    #because we cannot modify on string 'word'
    string = " ".join(temp)
    print(string)
    play(attempt, word, temp)

def loop():                         #this function prints out the main menu
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