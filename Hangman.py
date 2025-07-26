import random
fruits = [
    "apple", "banana", "mango", "orange", "grapes",
    "pineapple", "watermelon", "papaya", "guava","strawberry",
    "blueberry","kiwi", "lychee",
    "cherry", "peach", "pear", "coconut", "lemon","Durian",
    "rambutan","salak","feijoa","jabuticaba","cupuaçu","miracle Fruit",
    "ackee"
]
word = random.choice(fruits)
# print(word)
# Randomly select a fruit
guessed_letters = []
attempts = 10
# Show underscores for each letter
# display = ["_" for letter in word]

print("Guess the fruit name!")
while attempts > 0:
    display = [letter if letter in guessed_letters else "_" for letter in word]
    print(" ".join(display))

    guess = input("Guess a letter: ").lower()

    if guess in word:
        guessed_letters.append(guess)
        if all(letter in guessed_letters for letter in word):
            print("You guessed it! The word was:", word)
            break
    else:
        print("Wrong guess!")
        attempts -= 1
        print("Attempts left: ",attempts)

if attempts == 0:
    print("Out of attempts. The word was:", word)

