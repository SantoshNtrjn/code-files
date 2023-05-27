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
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
liste = [rock,paper,scissors]
user_choice = int(input("Enter your choice: 0 for rock, 1 for paper, 2 for scissors: "))
computer_choice = random.randint(0,2)
print(f'User Choice:\n{liste[user_choice]}\n')
print(f'Computer Choice:\n{liste[computer_choice]}\n')
if computer_choice == user_choice:
    print("Draw!")
elif computer_choice == 0 and user_choice == 2 :
    print("Computer Wins!")
elif computer_choice == 2 and user_choice == 0 :
    print("User wins!")
elif computer_choice > user_choice:
    print("Computer Wins!")
elif user_choice > computer_choice:
    print("User wins!")
