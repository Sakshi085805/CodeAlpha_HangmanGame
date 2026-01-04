import random 
from hangman_art import hangman_art
from word_list import letters, category

count = len(hangman_art)
name = input("\nEnter your name: ").title()

print(f"\nSelect the category from following list:\n\n{list(category.keys())}")

category_key = input("\nEnter the category name: ").lower()

chosen_word = random.choice(category[category_key])

word = []
display = " "

for letter in chosen_word:
    word +=  "_"
    display += letter

print(f"\nCan you guess the word:\n\n{word}\n")

wrong_count = 0

while not wrong_count >= count:
    chosen_letter = input("\nEnter the letter: ").lower()

    if chosen_letter in letters:
        letters.remove(chosen_letter)

        if not chosen_letter in chosen_word:
            print(hangman_art[wrong_count])
            wrong_count += 1

        for index, letter in enumerate(chosen_word):
            if letter == chosen_letter:
                word[index] = chosen_letter
        print(f"\n{word}")

        if not "_" in word:
            print(f"\nCongratulation! {name}, you win the game!")
            break

        if wrong_count == count:
            print(f"\nSorry! {name} , you lose the game!")
            break
    else:
        print(f"\n{chosen_letter} is already gone, enter another letter.\n")

print(f"\nThe word you had to guess is: {display.upper()}\n\nGamw Over!\n")
        

