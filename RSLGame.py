import time
import random
print ('Welcome to RSL game!')
time.sleep(1)
name = input('Please input your name: ')
print (f'Hello {name}!')
player_select = 0
computer_guess = 0
while player_select != 'e':
    player_select = input('Select scisser - s, rock - r, leaf - l, exit - e: ')
    time.sleep(1)
    computer_guess = random.randint(1,3)
    if computer_guess == 1:
        computer_guess = 's'
    elif computer_guess == 2:
        computer_guess = 'r'
    else: computer_guess = 'l'

    if player_select == computer_guess:
        print ("Draw!!!")
    if player_select == 's' and computer_guess == 'r':
        print (f'You lose! Computer choose: {computer_guess}')
    if player_select == 'r' and computer_guess == 'l':
        print (f'You lose! Computer choose: {computer_guess}')
    if player_select == 'l' and computer_guess == 's':
        print (f'You lose! Computer choose: {computer_guess}')
    if player_select == 's' and computer_guess == 'l':
        print (f"Congratulations! You're winner")
    if player_select == 'r' and computer_guess == 's':
        print (f"Congratulations! You're winner")
    if player_select == 'l' and computer_guess == 'r':
        print (f"Congratulations! You're winner")
print ('Goodbye, see you again!!')
exit()

