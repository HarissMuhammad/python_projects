import random
import time as tm
def main():
    try:
        print("Hello from guessing-number-game!")
        print("You have to guess between 1-100")
        tm.sleep(1)
        num = None
        rand = random.randint(1,100)
        while num != rand:
            num = int(input("Enter the number :"))
            
            if num<1 or num>100:
                print("Enter the number in range")
                continue
            elif num > rand +3:
                print("Too high")
            elif num > rand:
                print("Close but still high")
            elif num < rand -3:
                print("Too low")
            elif num<rand:
                print("Close but still low")
            else:
                print("You Guessed it!")
            
    except ValueError:
        print("Invalid Input!")
    except Exception as e:
        print(f"{e}")


if __name__ == "__main__":
    main()
