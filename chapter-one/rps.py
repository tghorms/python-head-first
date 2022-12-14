import random

selections = ['rock', 'paper', 'scissors']

user_input = input("rock, paper, scissors? ")
comp_choice = random.choice(selections)
print('The computer choses ' + comp_choice)
if user_input != 'rock' or user_input != 'paper' or user_input != 'scissors':
    print('Invaild response')

if user_input == 'rock' and comp_choice == 'rock': 
    print('User tied :(')
elif user_input == 'rock' and comp_choice == 'scissors':
    print('User Won!!!')
elif user_input == 'paper' and comp_choice == 'paper': 
    print('User tied :(')
elif user_input == 'paper' and comp_choice == 'rock':
    print('User Won!!!')
elif user_input == 'scissors' and comp_choice == 'scissors': 
    print('User tied :(')
elif user_input == 'scissors' and comp_choice == 'paper':
    print('User Won!!!')
else:
    print('Comp won, suck it Loser!')