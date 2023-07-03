import random

print("Welcome to Hangman game!")

words = ["apple", "banana", "orange", "mango", "peach", "grape", "kiwi"]
secret_word = random.choice(words)
letters = set(secret_word)
used_letters = set()
lives = 3

while len(letters) > 0 and lives > 0:
    print("You have", lives, "lives left and you have used these letters:", " ".join(used_letters))
    
    word_list = [letter if letter in used_letters else "-" for letter in secret_word]
    print("Current word: ", " ".join(word_list))
    
    user_letter = input("Guess a letter: ").lower()
    
    if user_letter in letters:
        letters.remove(user_letter)
        used_letters.add(user_letter)
    else:
        lives -= 1
        used_letters.add(user_letter)
    
if lives == 0:
    print("Sorry, you died. The word was", secret_word)
else:
    print("Congratulations! You guessed the word", secret_word, "in", len(used_letters), "tries.")