import random
computer_score = 0
player_score = 0

backend_dict = {'snake' : 1, 'water':0, 'gun':-1}
reverse_backend_dict = { v : k for k, v in backend_dict.items()}



while computer_score <2 and player_score < 2:

    while True:
        user_choice = input('Snake,Water,Gun : ').lower()
        if user_choice == 'exit':
            print('game closed')
            quit()
        if user_choice in ['snake','water','gun']:
            break
        else :
            print('Wrong input')

    user_input = backend_dict[user_choice]
    computer_input = random.choice([1,0,-1])

    print(f'Player chose : {user_choice}')
    print(f'Computer chose : {reverse_backend_dict[computer_input]}')


    result = computer_input - user_input

    if result == 0:
        print('Draw')
    if result == 1 or result == -2:
        print('Computer Wins')
        computer_score += 1
    if result == 2 or result == -1:
        print('Player Wins')
        player_score += 1    

    print(f'Player Score : {player_score}')
    print(f'Computer Score : {computer_score}')


if player_score == 2:
    print('\n🎉 You won the Best of 3 Match!')

else:
    print('\n💻 Computer won the Best of 3 Match!')
        
        
    