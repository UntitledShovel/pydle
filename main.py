import requests, json, random, time, os
from termcolor import colored

url = "https://random-word-api.herokuapp.com/word?length=5"
response = requests.get(url)
response = json.loads(response.text)
word = response[0]
url = "https://random-word-api.herokuapp.com/all"
response = requests.get(url)
dictionary = json.loads(response.text)
greyLetters = []
big_keyboard = "Q W E R T Y U I O P\nA S D F G H J K L\nZ X C V B N M"
title_lines = ["░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░"
, "░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗"
, "░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║"
, "░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║"
, "░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝"
, "░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░"
, " "
, "██████╗░██╗░░░██╗██████╗░██╗░░░░░███████╗"
, "██╔══██╗╚██╗░██╔╝██╔══██╗██║░░░░░██╔════╝"
, "██████╔╝░╚████╔╝░██║░░██║██║░░░░░█████╗░░"
, "██╔═══╝░░░╚██╔╝░░██║░░██║██║░░░░░██╔══╝░░"
, "██║░░░░░░░░██║░░░██████╔╝███████╗███████╗"
, "╚═╝░░░░░░░░╚═╝░░░╚═════╝░╚══════╝╚══════╝"]
letters_added_to_keyboard = []

def print_title():
    global title_lines
    counter = 0

    for line in title_lines:
        if counter > 5:
            print(colored(line, "yellow"))
        else:
            print(colored(line, "cyan"))
        time.sleep(.5)
        counter += 1

def colorcode(wordGuessed):
    global word, colors, greyLetters, emoji_render
    wordGuessed = [char for char in wordGuessed.lower()]
    orangeLetters = []

    for i in range(len(wordGuessed)):
        if wordGuessed[i] == word[i]:
            wordGuessed[i] = colored(wordGuessed[i], "green")
        elif wordGuessed[i] in word:
            if wordGuessed[i] not in orangeLetters:
                orangeLetters.append(wordGuessed[i])
                wordGuessed[i] = colored(wordGuessed[i], "yellow")
            else:
                if wordGuessed[i] not in greyLetters:
                    greyLetters.append(wordGuessed[i])             
                    wordGuessed[i] = colored(wordGuessed[i], "dark_grey")
        else:
            if wordGuessed[i] not in greyLetters:
                greyLetters.append(wordGuessed[i])
            wordGuessed[i] = colored(wordGuessed[i], "dark_grey")
    return ''.join(wordGuessed)



def main():
    global word, dictionary, greyLetters, big_keyboard, letters_added_to_keyboard
    guessesLeft = 6
    print_title()
    while guessesLeft > 0:
        if len(greyLetters) > 0:
            for letter in greyLetters:
                big_keyboard = big_keyboard.replace(letter.upper(), colored(letter.upper(), "dark_grey"))
                letters_added_to_keyboard.append(letter)
        x = input(f'Try and guess the word, You have {guessesLeft} guesses left\n{big_keyboard}\n> ')
        if not len(x) == 5:
            print('You must guess a 5 letter word')
            continue
        if not x.lower() in dictionary:
            print('That is not a word')
            continue
        if x.lower() == word:
            print(f'You guessed the word {word}!')
            break
        else:
            print(colorcode(x.lower()))
            guessesLeft -= 1
            if guessesLeft == 0:
                print(f'You lost, the word was {word}')
                break

if __name__ == '__main__':
    main()
    os.system("pause")
