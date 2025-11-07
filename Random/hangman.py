## Hangman Game Configuration
string = "word"
attempts = 6
emptyString = ["-"]*len(string)

while attempts != 0:
    if "".join(emptyString) == string:
        print("Congratulations! You've guessed the word:", string)
        break
    guess = input("Enter a letter: ")
    guess = guess.lower()
    if guess in string.lower():
        index = string.index(guess)
        emptyString[index] = guess
        print("".join(emptyString))
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")

if attempts == 0:
    print("Game Over! You've run out of attempts. The word was:", string)