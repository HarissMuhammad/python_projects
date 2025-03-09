import random
from words_file import words
from hangman_visual import lives_visual_dict
def main():
    print("Hello from hangman!")

    def get_valid_word(words):
        word = random.choice(words)
        while "-" in word or " " in word:
            word = random.choice(words)
        
        return word.upper()
    
    
    
    def hangman():
        lives = 7
        used_letters = set()
        word_letters = get_valid_word(words)
        hidden = ["_" for _ in word_letters]
        print(" ".join(hidden))
        while True:
            guessed_letters = input("Guess the Letters : ").upper()
            print(f"You Guessed : {guessed_letters}")
            
            if guessed_letters not in word_letters:
                print("Incorrect")


            
            for j, letter in enumerate(word_letters):
                if letter == guessed_letters:
                    hidden[j] = guessed_letters
                
            print("Word to guess", " ".join(hidden))
                
            
            if guessed_letters in used_letters:
                print("You have already Guessed this letter")
            else:
                used_letters.add(guessed_letters)
                
            
            if guessed_letters not in word_letters:
                lives -= 1 
                print(f"Wrong Answer you have {lives} Lives left")
                print(lives_visual_dict[lives])
                
            if lives == 0:
                print(f"You lose! The word was {word_letters}")
                break
            elif "_" not in hidden:
                print("You win!")
                break
    hangman()
    


if __name__ == "__main__":
    main()
