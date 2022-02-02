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

#Write your code below this line 👇
import random
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors "))

possibilities = [rock, paper, scissors]
print(f"You choose\n{possibilities[choice]}")
computer_choice = random.randint(0, 2)
print(f"The computer chose\n{possibilities[computer_choice]}")

if choice == 0:
  if computer_choice == 0:
    print("You tie")
  elif computer_choice == 1:
    print("You Lose")
  else:
    print("You win!")
elif choice == 1:
  if computer_choice == 0:
    print("You Win!")
  elif computer_choice == 1:
    print("You tie")
  else:
    print("You lose")
else:
  if computer_choice == 0:
    print("You lose")
  elif computer_choice == 1:
    print("You win!")
  else:
    print("You tie")