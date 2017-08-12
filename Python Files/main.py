from random import shuffle
hearts = [1,2,3,4,5,6,7,8,9,10,10,10,10]
spades = [1,2,3,4,5,6,7,8,9,10,10,10,10]
diamonds = [1,2,3,4,5,6,7,8,9,10,10,10,10]
deck = hearts+spades+diamonds
shuffle(deck)
dealer_hand = []
player_hand = []
while True:
    if len(player_hand) <2:
        player_hand.append(deck[0])
        del deck[0]
    if len(dealer_hand) < 2:
        dealer_hand.append(deck[0])
        del deck[0]
    if len(dealer_hand) == 2 and len(player_hand) == 2:
        break
print('Your hand')
player_total = 0
player_hand.sort(reverse=True)
for i in player_hand:
    print(i)
    if i == 1:
        ace = int(input("You have an ace, do you want it to be an 11 or 1?: "))
        if ace == 11:
            print(i)
    player_total += i
print('Dealers Hand')
print(dealer_hand[0])
print("?")
if player_total >21:
    dealer_total = 0
    for i in dealer_hand:
        dealer_total += i
    if dealer_total > 21:
        print("You win, dealer is over 21")
    else:
        print("You lose")
if player_total == 21:
    print("YOU WIN")


while True:
    hit = input("Would you like a new card?(y/n): ").lower()
    if hit == 'y':
        player_hand.append(deck[0])
        del deck[0]
        print("NEW HAND")
        player_hand.sort(reverse=True)
        for i in player_hand:
            print(i)
            if i == 1:
                ace = int(input("You have an ace, do you want it to be an 11 or 1?: "))
                if ace == 11:
                    print(i)
            player_total += i
        player_total = 0
        for i in player_hand:
            player_total += i
        if player_total > 21:
            dealer_total = 0
            for i in dealer_hand:
                dealer_total += i
            print("DEALER TOTAL")
            print(dealer_total)
            while dealer_total < 17:
                dealer_hand.append(deck[0])
                del deck[0]
                dealer_total = 0
                for i in dealer_hand:
                    dealer_total += i
                print("DEALER NEW TOTAL")
                print(dealer_total)
            if dealer_total > 21:
                print("YOU WIN")
                break
            elif dealer_total == 21:
                if player_total == 21:
                    print("YOU WIN")
                    break
                else:
                    print("YOU LOSE")
                    break
            elif player_total > dealer_total and (player_total < 21 and dealer_total < 21):
                print("YOU WIN")
                break
            else:
                print("YOU LOSE")
                break

    else:
        dealer_total = 0
        for i in dealer_hand:
            dealer_total += i
        print("DEALER TOTAL")
        print(dealer_total)
        while dealer_total < 17:
            dealer_hand.append(deck[0])
            del deck[0]
            dealer_total = 0
            for i in dealer_hand:
                dealer_total += i
            print("DEALER NEW TOTAL")
            print(dealer_total)
        if dealer_total > 21:
            print("YOU WIN")
            break
        elif dealer_total == 21:
            if player_total == 21:
                print("YOU WIN")
                break
            else:
                print("YOU LOSE")
                break
        elif player_total > dealer_total and (player_total < 21 and dealer_total < 21):
            print("YOU WIN")
            break
        else:
            print("YOU LOSE")
            break
