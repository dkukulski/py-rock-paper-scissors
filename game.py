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

print("Game rock | paper | scissors")
choose = input("Choose: r = rock | p = paper | s = scissors\n")
computer_choose = (random.randint(0, 2))

if(choose == "r"):
  print(rock)
  print("-------------------------------")
  if(computer_choose == 0):
    print(rock)
    print("DRAW")
  elif(computer_choose == 1):
    print(paper)
    print("You Lost")
  else:
    print(scissors)
    print("You WON!! :)")
elif(choose == "p"):
  print(paper)
  print("-------------------------------")
  if(computer_choose == 0):
    print(rock)
    print("You WON!! :)")
  elif(computer_choose == 1):
    print(paper)
    print("DRAW")
  else:
    print(scissors)
    print("You Lost")
else:
  print(scissors)
  print("-------------------------------")
  if(computer_choose == 0):
    print(rock)
    print("You Lost")
  elif(computer_choose == 1):
    print(paper)
    print("You WON")
  else:
    print(scissors)
    print("DRAW")  
