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
a = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if choice >= 3 or choice < 0:
    print("You type an invalid number, you lose!")
else:
    print(a[choice])

    print("Computer Chose: ")

    AIchoice = random.randint(0,2)

    print(a[AIchoice])

    if choice == 0 and AIchoice == 2:
        print("You win!")
    elif AIchoice == 0 and choice == 2:
        print("You lose")
    elif AIchoice > choice:
        print("You lose")
    elif choice > AIchoice:
        print("You win")
    elif AIchoice == choice:
        print("It's a Draw")