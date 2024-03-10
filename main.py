import random
import string
import wordlist as words
import hangmanArt as hangman

def printD():
    for letter in display:
        print(letter ,end=" ")
    print("\n")


display=[]
game_end=False
life_number=6
chosen_word=random.choice(words.word_list).lower().strip()
word_lenght=len(chosen_word)
for i in range(word_lenght):
    display.append("_")
print("Welcome to Hangman..\n You have " + str(life_number) +" lives\n" + hangman.stages[0])
while not game_end:
    guess=input("Guess a letter: ").lower()
    for position in range(word_lenght):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=guess
    printD()
    if guess not in chosen_word:
        life_number-=1
        print(hangman.stages[life_number])
        print("You have " + str(life_number) + " lives left")
        if life_number==0:
            game_end=True
            print("You lose, the word was "+ chosen_word)
            break

    if "_" not in display:
        print("You won!")
        game_end=True
        printD()
