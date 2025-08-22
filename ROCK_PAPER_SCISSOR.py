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
game =[rock, paper, scissors]
r = random.choice(game)
print("""-----------------------------ROCK PAPER SCISSOR GAME----------------------------------\n\n
                  ENTER [ R ] FOR ROCK
                        [ S ] FOR SCISSIOR 
                        [ P ] FOR PAPER""")

c = input("Enter your choice :   ").upper()

if c == "R":
    print("your choice : ",rock )
    print("computer choice : ", r)
    if r ==rock:
        print("_________DRAW________\n")
    elif r == scissors:
        print("_________YOU WON________\n")
    else:
        print("_________YOU LOST________\n")
elif c == "S":
    print("your choice\n",scissors )
    print("computer choice\n", r)
    if r ==rock:
        print("_________YOU LOST________\n")
    elif r == scissors:
        print("_________DRAW________\n")
    else:
        print("_________YOU WON________\n")
elif c == "P":
    print("your choice\n",paper)
    print("computer choice\n", r)
    if r ==rock:
        print("_________YOU WON________\n")
    elif r == scissors:
        print("_________YOU LOST________\n")
    else:
        print("_________DRAW________\n")
else:
    print("Wrong choice\n")
print("------------END------------")



