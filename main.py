
import random


print("Welcome to rock paper scissors game")
# keeping tract of there scores
user_score = 0
cpu_score = 0
count = 1
while count < 3:
    print("Playing")
    start = True
   
    user_input = input("pick an option between 'R', 'P' or 'S': ")
    command = ['R', 'P', 'S']
    while user_input not in command:
        print("select a valid option")
        user_input = input("pick an option between 'R', 'P' or 'S': ")
    cpu_input = random.choice(command)
    print(f"Player(Rock) = {user_input}: CPU(Paper) = {cpu_input}")

    # checking to see who won
    if(cpu_input != user_input):
        if(cpu_input == 'R' and user_input == 'S'):
            cpu_score += 1
        elif(cpu_input == 'S' and user_input == 'P'):
            cpu_score += 1
        elif(cpu_input == 'P' and user_input == 'R'):
            cpu_score += 1
        else:
            user_score += 1
        count += 1
    elif(cpu_input == user_input):
        # if the inputs are thesame we reset the counter to start#|
        count = 1
    



if(cpu_score >= 2):
    print(f"CPU Won with {cpu_score} points")
           
if(user_score >= 2):
    print(f"You Won with {user_score} points")



