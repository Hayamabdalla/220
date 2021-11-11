"""
Name: Hayam Abdalla
lab11.py
"""
from random import randint


def get_words(wordlist):
    file = open(wordlist, "r")
    lines = file.readlines()
    words = []
    for word in lines:
        word = word.replace("\n", "")
        words.append(word)
    file.close()
    return words


def pick_word(words):
    secret_word = words[randint(1, len(words))]
    return secret_word


def guess_word(secret_word, guess_letters, guessed_word, letter):
    check = False
    for i in range(len(secret_word)):
        if secret_word[i] == letter:
            guessed_word[i] = letter
            check = True
    if check:
        return True
    guess_letters.append(letter)
    return False


def word_spelled(guess_word, secret_word):
    if "".join(guess_word) == secret_word:
        return True
    else:
        return False


def guess_letter(guessed_letters, turn_count, secret_word, guessed_word):
    letter = input("Guess a Letter: ")
    letter = letter.lower()
    check = False
    while check == False:
        check = True
        for ch in guessed_letters:
            if letter == ch:
                print("This letter has already been guessed, try again.")
                letter = input("Guess a letter: ")
                letter = letter.lower()
                check = False
        if (len(letter) != 1) or not (ord(letter) > 97 and ord(letter) <= 121):
            print("This is an invalid entry, try again")
            letter = input("guess a letter: ")
            letter = letter.lower()
            check = False
    if guess_word(secret_word, guessed_letters, guessed_word,turn_count, letter):
        return True
    else:
        return False


def print_board(guessed_word, turn_count, guessed_letters):
    print("--" + ("-----" * len(guessed_word)) + "--")
    print(guessed_word)
    print("--" + ("-----" * len(guessed_word)) + "--")
    print()
    print("number of guesses: " +str(turn_count))
    print("guessed letters: "+ str(guessed_letters))


def play_game():
    words = get_words("list.txt")
    secret_word = pick_word(words)
    guessed_word = [" "] * len(secret_word)
    guessed_letters = []
    trun_count = 0
    print_board(guessed_word, guessed_letters)
    while turn_count < 7 and not word_spelled(guessed_word, secret_word):
        if guess_letter(guessed_letters,trun_count secret_word, guessed_word) == False:
            turn_count += 1
            print_board(guessed_word, turn_count, guessed_letters)
    if turn_count >= 7:
        print("You are out of turns, Game Over")
    else:
        print("you have won the game!")
