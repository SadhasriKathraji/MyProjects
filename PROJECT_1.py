import random
rock = '''
 _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images =[rock,paper,scissors]
user_choice = int(input("enter the any number from 0 to 2 (0 for rock, 1 for paper, 2 for scissors):"))
print("you chose:",game_images[user_choice])
if user_choice >2 or user_choice<0:
    print("you entered an invalid number")
else:
    computer_choice = random.randint(0,2)
    print("computer chose:",game_images[computer_choice])

    if user_choice == computer_choice:
        print("game is drawn")
    elif user_choice == 0 and computer_choice ==2:
        print("you win")
    elif computer_choice == 0 and user_choice ==2:
        print("you lose")
    elif computer_choice > user_choice: #2>0
        print("you lose")
    elif user_choice > computer_choice: #2>0
        print("you win")



