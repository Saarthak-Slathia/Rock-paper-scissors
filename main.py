# Rock, Paper and Scissors game in Python
import random

def game():
    user = int(input("[Users turn] - Rock (1), Paper (2) or Scissors (3):  "))
    computer = random.randint(1,3)

    if user == computer:
        print("Drawn !!!")
        print(user)
        print(computer)
        
    elif user == 1 and computer == 2:
        print("Paper traps rock. Computer Won")
        print(user)
        print(computer)
        
    elif user == 2 and computer == 1:
        print("Paper traps rock. You Won !!!")
        print(user)
        print(computer)
        
    elif user == 2 and computer == 3:
        print("Scissor cuts Paper. Computer Won.")
        print(user)
        print(computer)
        
    elif user == 3 and computer == 2:
        print("Scissor cuts Paper. You Won !!!")
        print(user)
        print(computer)
        
    elif user == 1 and computer == 3:
        print("Rock breaks Scissor. You Won !!!")
        print(user)
        print(computer)

    elif user == 3 and computer == 1:
        print("Rock breaks Scissor. Computer Won.")
        print(user)
        print(computer)

    else:
        print("Invalid Input !!! :~{")

    return None

while True:
    game()
