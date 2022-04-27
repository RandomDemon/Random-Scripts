import random
import time

number = random.randint(1, 100)
score = float(1)

print("The goal of the game is to guess the number, and get the lowest score possible!")
time.sleep(1)
print("You will be told if the number you guessed is greater or lesser than the actual number!")
time.sleep(1)
print("Pick a number between 1 and 100!")

while True:
    guess = float(input("Enter your guess!"))
    time.sleep(1)
    if guess == number:
        time.sleep(1)
        print("You win!")
        time.sleep(1)
        print("Final score: ", score)
        break
    if guess > number:
        print("The number is lower than", guess)
        score = score + 1
        time.sleep(1)
    if guess < number:
        print("The number is greater than", guess)
        score = score + 1
        time.sleep(1)
