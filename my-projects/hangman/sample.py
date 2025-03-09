import string
import random
from words import words
from hangman_visual import lives_visual_dict

rand_word = random.choice(words)
print("-" for _ in rand_word)
# rand_letters = list(set(rand_word))
# print(rand_letters)
# user_input = list(set(input("Guess the letter")))
# if user_input in rand_letters:
    # print("Correct")
    
# print(rand_letters[1])
