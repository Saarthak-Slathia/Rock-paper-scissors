# Snake, Water and Gun game in Python
import random

def game():
    user = int(input("[Users turn] - Snake (1), Water (2) or Gun (3):  "))
    computer = random.randint(1,3)

    if user == computer:
        print("Drawn !!!")
        print(user)
        print(computer)
        
    elif user == 1 and computer == 2:
        print("Snake beat water. You Won !!!")
        print(user)
        print(computer)
        
    elif user == 2 and computer == 1:
        print("Snake beat water. Computer Won.")
        print(user)
        print(computer)
        
    elif user == 2 and computer == 3:
        print("Water beat gun. You Won !!!")
        print(user)
        print(computer)
        
    elif user == 3 and computer == 2:
        print("Water beat Gun. Computer Won.")
        print(user)
        print(computer)
        
    elif user == 1 and computer == 3:
        print("Gun beat snake. Computer Won.")
        print(user)
        print(computer)

    elif user == 3 and computer == 1:
        print("Gun beat snake. You Won !!!")
        print(user)
        print(computer)

    else:
        print("Invalid Input !!! :~{")

    return None

game()