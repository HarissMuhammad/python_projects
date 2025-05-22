# Hangman Game 🎩 (Console Word Guessing Game)

![GitHub Repo stars](https://img.shields.io/github/stars/HarissMuhammad/python_projects?style=social)
![GitHub forks](https://img.shields.io/github/forks/HarissMuhammad/python_projects?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/HarissMuhammad/python_projects)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A classic console-based Hangman game written in Python. Try to guess the hidden word letter-by-letter before you run out of lives.

---

## 📌 Features

- Randomly selects a word from a predefined word list
- Displays underscores for unknown letters
- Reveals correct guesses and tracks incorrect ones
- ASCII-based visual hangman stages
- Prevents duplicate guesses and handles invalid input

---

## 🚀 How to Run the App

### 📥 1. Clone the Repository

```bash
git clone https://github.com/HarissMuhammad/python_projects.git
cd python_projects/hangman
```
### 📦 2. Ensure Required Files

Make sure these files are in the same folder:

    hangman.py (your main game file)

    words_file.py (contains a words list)

    hangman_visual.py (contains a lives_visual_dict dictionary)

### ▶️ 3. Run the Script
```bash
python main.py
```
### 🎮 How the Game Works

    A word is randomly selected and hidden as underscores.

    You guess one letter at a time.

    If the guess is correct, it is revealed in the word.

    If incorrect, you lose a life and progress toward the hangman drawing.

    You win by guessing all letters or lose if you run out of lives.

### 🧠 Technologies Used

    Python 3

    Built-in libraries: random
