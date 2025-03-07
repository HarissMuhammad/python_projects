import time as tm
import random

def main():
    print("Hello from guessing-number-game-computer!")
    
    print("Hello from guessing-number-game!")
    print("You have to think of a number between 1-10\
            And i will guess it")
    tm.sleep(1)
        
try:
    guess = [1,2,3,4,5,6,7,8,9,10]
    response = ""
    while response != "yes" or "YES":
        a = random.choice(guess)
        response = input(f"Is it {a} : (yes/no)")
    print("i guessed it!")
except ValueError:
    print("Invalid Input")


if __name__ == "__main__":
    main()
