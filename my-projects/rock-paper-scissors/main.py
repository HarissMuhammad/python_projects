import time
import random
def main():
    try:
        print("Hello from rock-paper-scissors!\n")
        time.sleep(1)
        def play():
            user = int(input("Choose (1) for Rock-(2) for Paper-(3) for Scissors\n"))
            card = [1,2,3]
            rand = random.randint(1,3)
            if user < 1 or user >3:
                return "Invalid Input"
            if user == rand:
                return ("Tie")
            elif (user == 1 and rand ==2) or (user==2 and rand == 1) or\
                (user == 3 and rand == 2):
                    return ("You Won!")
        
            return ("I win! You LOSE")
            
              
        while True:
            a = play()
            print(a)
            a =input("Exit(yes/no)\n")   
            if a == "yes":
                break
            
            continue
    except ValueError:
        print("Enter Valid response")

if __name__ == "__main__":
    main()
