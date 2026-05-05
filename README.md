# Snowman-Meltdown

A fun word-guessing game where you try to save a snowman from melting! Similar to Hangman, but instead of drawing a
figure, you watch a snowman gradually melt away with each wrong guess.

## Description

Snowman Meltdown is a Python-based terminal game where players guess letters to reveal a hidden word. Each incorrect
guess causes the snowman to melt a little more. The goal is to guess the complete word before the snowman completely
melts away!

## Features

- Random word selection from a predefined word list
- ASCII art visualization of the snowman's melting stages
- Input validation for guesses
- Track of previously guessed letters
- Option to play multiple rounds

## Game Rules

1. A random word is selected from the word list
2. Players guess one letter at a time
3. Correct guesses reveal the letter's position(s) in the word
4. Incorrect guesses cause the snowman to melt (4 stages total)
5. Win by guessing all letters before the snowman completely melts
6. Lose if the snowman melts completely (3 wrong guesses maximum)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/Snowman-Meltdown.git
cd Snowman-Meltdown
```

## How to Play
Run the main game file:``` bash
python snowman.py
Follow the on-screen prompts:
Enter a single letter when prompted
The game will tell you if your guess is correct or wrong
Watch the snowman's status change with each incorrect guess
Try to guess the word before the snowman melts!

## Project Structure
Snowman-Meltdown/
│
├── snowman.py          # Main game entry point with word list
├── game_logic.py       # Core game logic and functions
├── ascii_art.py        # Snowman ASCII art stages
└── README.md           # This file

## Requirements
Python 3.x
No external dependencies required

## Contributing
Feel free to fork this project and submit pull requests with improvements or bug fixes!

## License
This project is open source and available for educational purposes.