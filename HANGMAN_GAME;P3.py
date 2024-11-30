import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']

print("Let's play Hangman Game!!!")
word_list = [
    "apple",
    "beautiful",
    "potato",
    "Python",
    "Programming",
    "Computer",
    "Algorithm",
    "Developer",
    "Hangman",
    "Artificial",
    "Intelligence",
    "Software",
    "Network",
    "Data",
    "Science",
    "Machine",
    "Learning",
    "Security",
    "Encryption",
    "Cloud",
    "Database",
    "Technology", ]
lives = 6
chosen_word = random.choice(word_list);
#print(chosen_word) # apple

display = []
for i in range(len(chosen_word)): # 0 1 2 3 4
    display += '_'
#print(display)
game_over = False
while not game_over:
    guessed_letter = input("guess a letter:") #a
# code to replace the dash with guessed letter
    for position in range(len(chosen_word)): # 0 1 2 3 4
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you lose!!")
    if '_' not in display:
        game_over = True
        print("you win!!")
    print(stages[lives])


