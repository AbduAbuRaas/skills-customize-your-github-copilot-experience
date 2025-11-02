# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a terminal-based Hangman game to practice string manipulation, loops, conditionals, and user input. Implement a clear game loop that selects a word, accepts guesses, shows progress, and reports win/lose outcomes.

## 📝 Tasks

### 🛠️	Implement Hangman core

#### Description
Create the playable Hangman game: choose a word, accept single-letter guesses, update and display progress, and enforce a limited number of incorrect attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list (at least 10 words).
- Accept single-letter guesses (case-insensitive) and show current progress in underscore format (e.g., _ a _ _ _).
- Track and display remaining incorrect guesses (suggested default: 6).
- End when the word is fully guessed or attempts are exhausted and display a clear win or lose message.
- Handle repeated guesses without subtracting additional attempts and inform the player when a letter was already guessed.

### 🛠️	Add polish and optional features

#### Description
Improve usability and robustness: validate input, allow replay, and optionally add hints or configurable difficulty.

#### Requirements
Completed program should include one or more of the following enhancements:

- Input validation (ignore non-letter input, require a single character).
- Option to play again after a game ends.
- Hint system (reveal one letter or show word length/difficulty).
- Load word lists from an external file or support difficulty levels.

Example gameplay:

```text
Welcome to Hangman!
_ _ _ _ _ _
Guess a letter: a
Good guess! Current word: _ a _ _ _ _
Incorrect guesses left: 6
Guess a letter: r
Sorry — no 'r'. Current word: _ a _ _ _ _
Incorrect guesses left: 5
...
```
