# Guessing Game
import random

#computer picks number at random based on difficulty (easy, medium, hard)
score = 100
tries = 5

def difficulty(user_choice):
        easy = random.randint(1, 5)
        medium = random.randint(1, 10)
        hard = random.randint(1, 50)

        if user_choice == "easy":
            difficulty_setting = easy
        elif user_choice == "medium":
            difficulty_setting = medium
        elif user_choice == "hard":
            difficulty_setting = hard
        else:
            difficulty_setting = easy

        return difficulty_setting

user_difficulty_choice = input("Pick a difficulty, easy, medium, hard: ")



while tries > 0 or user_guess == computer_num:


    
    computer_num = difficulty(user_difficulty_choice.lower())

    #User inputs guess, computer outputs response based on how close answer is to number, if guess is not a number within range computer lets the user know

    user_guess = input("Guess a number! easy (1 - 5), medium (1 - 10), hard (1 - 50): ")

    if int(user_guess) == int(computer_num):
        print("Correct!")
    elif int(user_guess) > int(computer_num):
        print("You guessed high.")
        print("Computer had picked, ",int(computer_num), "try again.")
    elif int(user_guess) < int(computer_num):
        print("You guessed low.")
        print("Computer had picked: ", int(computer_num), "try again.")
    tries -= 1
    #User gets score reduction with each guess

print(score)
    #after guess is correct final score is listed




    #later versions could have high score list


    #testing pull and push to github



