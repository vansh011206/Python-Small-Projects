import random


def game():
    print('Lets Begin the Snake water Gun game')
    keys = ['snake','water','gun']
    computer = random.choice(keys)
    user = input('Enter Your Choice(i.e snake,water,Gun): \n').lower()
    print(f'So Computer chose :{computer} ')
    if user not in keys:
        print("Invalid choice! Please select snake, water, or gun.")
        return
    if user == computer :
        print('Ohh! Game Tied')
    elif user == 'snake' and  computer == 'water':
        print('Yeahh! You Won') 
    elif user == 'water' and  computer == 'snake':
        print('Oops! You loose')
    elif user == 'gun' and  computer == 'water':
        print('Yeahh! You Won') 
    elif user == 'water' and  computer == 'gun':
        print('Oops! You loose')
    elif user == 'gun' and  computer == 'snake':
        print('Yeahh! You Won') 
    elif user == 'snake' and  computer == 'gun':
        print('Oops! You loose')
    else:
        print('...')

que = input("Wanna Play 'Snake, Water, and Gun'? Say yes or no: \n").lower()
if que == 'yes':
    while True:
        game()
        next_game = input("Do you want to play again? (yes/no): \n").lower()
        if next_game != 'yes':
            print('Thanks for your time, Bye!')
            break
else:
    print('Okay, maybe next time!')
