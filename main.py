import requests, json, random

url = "https://random-word-api.herokuapp.com/word?length=5"
response = requests.get(url)
response = json.loads(response.text)
word = response[0]
url = "https://random-word-api.herokuapp.com/all"
response = requests.get(url)
dictionary = json.loads(response.text)
greyLetters = []

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colorcode(wordGuessed):
    global word, colors, greyLetters
    wordGuessed = [char for char in wordGuessed.lower()]
    orangeLetters = []


    for i in range(len(wordGuessed)):
        if wordGuessed[i] == word[i]:
            wordGuessed[i] = colors.OKGREEN + wordGuessed[i] + colors.ENDC
        elif wordGuessed[i] in word:
            if wordGuessed[i] not in orangeLetters:
                orangeLetters.append(wordGuessed[i])
                wordGuessed[i] = colors.FAIL + wordGuessed[i] + colors.ENDC
            else:
                if wordGuessed[i] not in greyLetters:
                    greyLetters.append(wordGuessed[i])             
                wordGuessed[i] = colors.OKBLUE + wordGuessed[i] + colors.ENDC
        else:
            if wordGuessed[i] not in greyLetters:
                greyLetters.append(wordGuessed[i])
            wordGuessed[i] = colors.OKBLUE + wordGuessed[i] + colors.ENDC
    return ''.join(wordGuessed)



def main():
    global word, dictionary, greyLetters
    guessesLeft = 6
    print('Welcome to Pydle!')
    while guessesLeft > 0:
        x = input(f'Try and guess the word, You have {guessesLeft} guesses left\nYou can also see the letters that are not in the word by typing in "show greys"\n> ')
        if x == "show greys":
            print(greyLetters)
            continue
        elif not len(x) == 5:
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
