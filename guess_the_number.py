import random
import os

# Global variables
lives = 0
number = 0

def art():
    logo = r"""                                                                                                                                            
                      █                                                                ▀                                                    
 ▄ ▄▄   ▄   ▄  ▄▄▄▄▄  █▄▄▄    ▄▄▄    ▄ ▄▄          ▄▄▄▄  ▄   ▄   ▄▄▄    ▄▄▄    ▄▄▄   ▄▄▄    ▄ ▄▄    ▄▄▄▄          ▄▄▄▄   ▄▄▄   ▄▄▄▄▄   ▄▄▄  
 █▀  █  █   █  █ █ █  █▀ ▀█  █▀  █   █▀  ▀        █▀ ▀█  █   █  █▀  █  █   ▀  █   ▀    █    █▀  █  █▀ ▀█         █▀ ▀█  ▀   █  █ █ █  █▀  █ 
 █   █  █   █  █ █ █  █   █  █▀▀▀▀   █            █   █  █   █  █▀▀▀▀   ▀▀▀▄   ▀▀▀▄    █    █   █  █   █         █   █  ▄▀▀▀█  █ █ █  █▀▀▀▀ 
 █   █  ▀▄▄▀█  █ █ █  ██▄█▀  ▀█▄▄▀   █            ▀█▄▀█  ▀▄▄▀█  ▀█▄▄▀  ▀▄▄▄▀  ▀▄▄▄▀  ▄▄█▄▄  █   █  ▀█▄▀█         ▀█▄▀█  ▀▄▄▀█  █ █ █  ▀█▄▄▀ 
                                                   ▄  █                                             ▄  █          ▄  █                      
                                                    ▀▀                                               ▀▀            ▀▀                       """
    return print(logo)

def life():
    global lives
    lives -= 1
    if(lives > 0):
        print(f"You have {lives} attempts remaining to guess the number.")
    if lives == 0:
            print("You've run out of guesses, you lose.")
            print(f"The number was {number}\n")
            return('h')

def start():
    global lives, number
    print("Welcome to the Number Guessing Game!\n")
    level = input("""Choose a difficulty.   Easy = 10 lives    Hard = 5 lives
    Type [e] for Easy level [h] for hard level:
                \n""").lower()
    if level == 'e':
        lives = 10
    elif level == 'h':
        lives = 5
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    print("READY?")
    


def guess():
    global lives, number
    g = int(input("Make a guess: "))
    if g > number:
        if g - number <= 5:
            print("A bit high.")
            return life()
        print("Too high.")
        return life()
    elif g < number:
        if g - number >= -5:
            print("A bit low.")
            return life()
        print("Too low.")
        return life()
    
    

    
    # if g-number >=-5:
    #     if g -number<5:
    #         print("Too low")
    #         return life()
    #     print("A bit low")
    #     return life()
    # elif g-number <=5:
    #     if g -number >5:
    #         print("Too high")
    #         return life()
    #     print("A bit high")
    #     return life()

    else:
        print(f"You got it! The answer was {number}\n")
        return('i')


    
def game():
    art()
    start()
    print (number)
    while True:
        result = guess()
        if result == 'i' or result == 'h':
            break
        
    r = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if r == 'y':
        game()
        print("\n" * 50)
    else:
        print("Thank you for playing!")
    
    
    
game()
    
    
    
    
        
    




    