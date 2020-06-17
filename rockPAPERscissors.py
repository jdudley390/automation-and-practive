import random, sys

print('ROCK, PAPER, SCISSORS')

#initialize variables to 0
#initilized variables don't move past 1 why????
wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties)) #%s acts as a place holder for each of the variables that is listed after. They appear in that order
    while True: #main loop for player
        print('Choose your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        player_choice = input()
        if player_choice == 'q':
            sys.exit()
        if player_choice == 'r' or player_choice == 'p' or player_choice == 's':
            break
        print('Type r, p, s, or q please')

    if player_choice == 'r':
        print('Rock vs...')
    elif player_choice == 'p':
        print('Paper vs...')
    elif player_choice == 's':
        print('Scissors vs...')
    #assign random int to pick CPUs choice in R,P,S
    random_num = random.randint(1,3)
    if random_num == 1:
        CPU = 'r'
        print('Rock')
    elif random_num == 2:
        CPU = 'p'
        print('Paper')
    elif random_num == 3:
        CPU = 's'
        print('Scissors')

    if player_choice == CPU:
        print('TIE')
        ties =+ 1
    elif player_choice == 'r' and CPU == 'p':
        print('You lose')
        losses =+ 1
    elif player_choice == 'p' and CPU == 's':
        print('You lose')
        losses =+ 1
    elif player_choice == 's' and CPU == 'r':
        print('You lose')
        losses =+ 1
    elif player_choice == 'r' and CPU == 's':
        print('You win')
        wins =+ 1
    elif player_choice == 'p' and CPU == 'r':
        print('You win')
        wins =+ 1
    elif player_choice == 's' and CPU == 'p':
        print('You win')
        wins =+ 1