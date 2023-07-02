import os
import random
from Art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

begin = True
while begin: 
    print(logo)
    start = input("Do you want to play a game of blackjack? (y|n) :: ").lower()
    if start == "y":
        os.system('cls')
        run = True
    elif start == "n":
        begin = False

    while run:
        user_deck = []
        dealer_deck = []
        for _ in range(2):
            user_deck.append(random.choice(cards))
        sum_user = sum(user_deck)
        dealer_deck.append(random.choice(cards))

        print(f'you cards: {user_deck}  current score: {sum_user}\n computer first card: {dealer_deck[0]}') 
        again = input("Do you want to draw another card? (y|n) :: ").lower()
        if again == "y":
            user_deck.append(random.choice(cards))
            dealer_deck.append(random.choice(cards))
            sum_user = sum(user_deck)
            sum_deal = sum(dealer_deck)
            if sum_user > 21:
                run = False
                print(f'you cards: {user_deck}  current score: {sum_user}\n computer deck: {dealer_deck} computer score: {sum_deal}\n You went over!\nGame over.')
            elif sum_deal > 21:
                run = False
                print(f'you cards: {user_deck}  current score: {sum_user}\n computer deck: {dealer_deck} computer score: {sum_deal}\n Computer went nuts!\n You Win!')
        else:
            sum_deal = sum(dealer_deck)
            if sum_deal > sum_user:
                run = False
                print(f'you cards: {user_deck}  current score: {sum_user}\n computer deck: {dealer_deck} computer score: {sum_deal}\n Computer Scored Higher. Hail the Comp!')
            elif sum_user > sum_deal:
                run = False
                print(f'you cards: {user_deck}  current score: {sum_user}\n computer deck: {dealer_deck} computer score: {sum_deal}\n You aced it!\n You Win!')




