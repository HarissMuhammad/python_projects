import time


def main():

    def countdown(t):
        while t:
            min, sec = divmod(t, 60)
            timer = "{:02d}:{:02d}".format(min, sec)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1

    user = int(input("Enter time in Seconds : "))
    countdown(user)

    print(f"Ramadan Mubarak")


if __name__ == "__main__":
    main()
