import time
import random
import string


def main():
    print("Hello from password-generator!")

    def generator(n):
        nums = string.digits
        char = string.ascii_letters
        symb = string.punctuation
        for a in range(n):
            pswrd = random.choice(char + nums + symb)
            rep = set()
            if_rep = rep.add(pswrd)
            while if_rep == pswrd:
                continue
            print(pswrd, end="", flush=True)
            time.sleep(0.3)
            n -= 1

    a = int(input("how many length of characters do you want : "))
    generator(a)
    print("")


if __name__ == "__main__":
    main()
