import random
import time

Ace = 11
Jack = 10
Queen = 10
King = 10

cards = [Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King]

e = 0
Ace_21 = False
player_bal = 0
dealer_bal = 0
player_cards = []
dealer_cards = []
player_cards_total = 0
dealer_cards_total = 0
card = ''
move = ''
moves = 0


def get_card():
    return (int(cards[random.randrange(1, 13)]))


dealer_cards = [get_card()]
player_cards = [get_card(), get_card()]
player_cards_total = sum(player_cards)


def get_move():
    if moves == 0:
        print('\nDealer\'s cards: ', dealer_cards)
        print('Your cards: ', player_cards, '\nTotal: ', player_cards_total)
    move = input('Chose your next move: ')
    if move in ['h', 'Hit']:
        move = 'hit'
    elif move in ['s', 'Stand']:
        move = 'stand'
    return (move)


while player_cards_total < 21:
    player_cards_total = sum(player_cards)
    dealer_cards_total = sum(dealer_cards)
    if player_cards_total > 20:
        print('\n\n//////////////////////////\nDealer\'s cards: ', dealer_cards)
        print('Your cards: ', player_cards, '\nTotal: ', player_cards_total, '\n//////////////////////////')
        print('\nBUST\n')
        break
    move = get_move()

    if move == 'hit':
        player_cards.append(get_card())
    else:
        break

if player_cards_total > 21:
    print('You lose!!!')
elif player_cards_total == 21:
    print('Great job, you win')
else:
    print('\n\n//////////////////////////\nDEALER\'S TURN\n//////////////////////////')
    while dealer_cards_total < 20:
        if e == 0:
            dealer_cards.append(get_card())
            e = 1

        print('\n//////////////////////////\nDealer\'s cards: ', dealer_cards, '\n Dealer\'s Total: ',
              dealer_cards_total)
        print('Your cards: ', player_cards)
        print('Your Total: ', player_cards_total, '\n//////////////////////////')
        dealer_cards_total = sum(dealer_cards)
        dealer_cards.append(get_card())

if dealer_cards_total == 21:
    print('YOU LOSE')
elif dealer_cards_total > 21:
    print('DEALER BUSTED with ', dealer_cards_total, '\nYOU WIN!!!')
elif dealer_cards_total > player_cards_total and dealer_cards_total < 22:
    print('YOU LOSE')
elif player_cards_total < 22:
    print('YOU WIN')

# if player_cards == 21 and Ace in player_cards:
# Ace_21 = True
# if Ace in dealer_cards and dealer_cards_total > 20:
# Ace_21 = True
# elif Ace in player_cards and player_cards_total > 20:
# Ace_21 = True