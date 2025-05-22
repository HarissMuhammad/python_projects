# Password Generator 🔐 (Secure Random Password Creator)

![GitHub Repo stars](https://img.shields.io/github/stars/HarissMuhammad/python_projects?style=social)
![GitHub forks](https://img.shields.io/github/forks/HarissMuhammad/python_projects?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/HarissMuhammad/python_projects)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A Python-based command-line tool that generates strong, secure passwords using a mix of letters, numbers, and symbols — displayed character-by-character with a brief delay for extra visual appeal.

---

## 📌 Features

- Generates random passwords with:
  - Uppercase and lowercase letters
  - Digits
  - Punctuation symbols
- User-defined password length
- Simulated "typing" animation using `time.sleep`
- Lightweight and terminal-based

---

## 🚀 How to Run the App

### 📥 1. Clone the Repository

```bash
git clone https://github.com/HarissMuhammad/python_projects.git
cd python_projects/password-generator
```
### ▶️ 2. Run the Script
```bash
python main.py
```
### 💡 How It Works

    You input the desired password length.

    The program generates a random password using:

        string.ascii_letters

        string.digits

        string.punctuation

    Each character is printed with a slight delay to simulate typing.

    A secure and unique password is displayed.

### 🧠 Technologies Used

    Python 3

    Built-in libraries: random, string, time
