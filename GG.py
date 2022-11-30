# Guessing Game
import random

#computer picks number at random based on difficulty (easy, medium, hard)


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


computer_num = difficulty(user_difficulty_choice.lower())



#User inputs guess, computer outputs response based on how close answer is to number, if guess is not a number within range computer lets the user know

user_guess = input("Guess a number! easy (1 - 5), medium (1 - 10), hard (1 - 50): ")



#User gets score reduction with each guess


#after guess is correct final score is listed




#later versions could have high score list


#testing pull and push to github



