while True:
    user_choice = input('Choose between snake, water, gun : ').lower()
    if user_choice == 'exit':
        print('Game closed')
        quit()
    if user_choice in ['snake','water','gun']:
        break
    else:
        print('Wrong input')

# snake drinks water - snake wins
# water damages gun - water wins
# gun kills snake - gun wins

backend_dict = {'snake' : 1, 'water':0, 'gun':-1}
reverse_backend_dict = { v : k for k, v in backend_dict.items()}

user_input = backend_dict[user_choice]

import random

computer_input = random.choice([1,0,-1])

print(f'Player chose : {user_choice}')
print(f'Computer chose : {reverse_backend_dict[computer_input]}')

# if computer_input ==  user_input:
#     print ('Match Draw')
# else:
#     if computer_input == -1 and user_input == 0:
#         print('Player Wins')
#     if computer_input == -1 and user_input == 1:
#         print('Computer Wins')
#     if computer_input == 0 and user_input == 1:
#         print('Player Wins')
#     if computer_input == 0 and user_input == -1:
#         print('Computer Wins')
#     if computer_input == 1 and user_input == 0:
#         print('Computer Wins')
#     if computer_input == 1 and user_input == -1:
#         print('Player Wins')


result = computer_input - user_input
if result == 0:
    print('Draw')
if result == 1 or result == -2:
    print('Computer Wins')
if result == 2 or result == -1:
    print('Player Wins')
