import random
import time as tm
def main():
    try:
        print("Hello from guessing-number-game!")
        print("You have to guess between 1-10")
        tm.sleep(1)
        num = None
        rand = random.randint(1,10)
        while num != rand:
            num = int(input("Enter the number :"))
            
            if num<1 or num>10:
                raise ValueError("Enter the number in range")
                continue
            elif num == rand:
                print("You Guessed it!")
            else:
                print("Try Again :(")
                continue
    except ValueError:
        print("Enter a valid number")
    except Exception as e:
        print(f"An Error occured {e} : ")


if __name__ == "__main__":
    main()
