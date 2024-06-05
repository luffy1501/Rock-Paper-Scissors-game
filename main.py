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
a = int(input("What do you wanna choose? type 0 for rock, 1 for scisscors and 2 for paper  "))

b = random.randint (0,2)
# print("Your choice:")
# print("Computers choice:")
if a == 0 and b == 2:
    print("Your choice:")
    print(rock)
    print("Computers choice:")
    print(paper)
    print("You lose")
if a == 0 and b ==1:
    print("Your choice:")
    print(rock)
    print("Computers choice:")
    print(scissors)
    print("You win")
if a == 0 and b == 0:
    print("Your choice:")
    print(rock)
    print("Computers choice:")
    print(rock)
    print("Draw")
if a == 1 and b == 0:
    print("Your choice:")
    print(scissors)
    print("Computers choice:")
    print(rock)
    print("You lose")
if a == 1 and b == 1:
    print("Your choice:")
    print(scissors)
    print("Computers choice:")
    print(scissors)
    print("You draw")
if a == 1 and b ==2:
    print("Your choice:")
    print(scissors)
    print("Computers choice:")
    print(paper)
    print("You win")
if a == 2 and b == 1:
    print("Your choice:")
    print(paper)
    print("Computers choice:")
    print(scissors)
    print("You lose")
if a == 2 and b == 2:
    print("Your choice:")
    print(paper)
    print("Computers choice:")
    print(paper)
    print("You draw")
if a == 2 and b ==0:
    print("Your choice:")
    print(paper)
    print("Computers choice:")
    print(rock)
    print("You win")
    
