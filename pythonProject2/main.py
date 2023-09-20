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
while True:
    number = int(input("What do you choose? (type 0 for Rock, type 1 for Paper, type 2 for Scissors)  "))

    if number == 0:
        print ("You choose rock:\n", rock)
    if number == 1:
        print ("You choose paper:\n", paper)
    if number == 2:
        print ("You choose scissors:\n", scissors)
    computer = random.randint(0, 2)

    if computer == 0:
        print ("computer choose rock:\n", rock)
    if computer == 1:
        print ("computer choose paper:\n", paper)
    if computer == 2:
        print ("computer choose scissors:\n", scissors)


    if number == computer:
        print("No one lose ")

    if number == 0 and computer == 2:
        print("You win ")
    elif number == 2 and computer == 0:
        print("Computer win ")



    if number == 2 and computer == 1:
        print("You win ")
    elif number == 1 and computer == 2:
        print("Computer win ")



    if number == 1 and computer == 0:
        print("You win ")
    elif number == 0 and computer == 1:
        print("Computer win ")

    finish = input("Do you want play one more time? (Yes or No): ")

    if finish == 'Yes' or finish == 'yes':
        continue
    else:
        print('You finished')
        break