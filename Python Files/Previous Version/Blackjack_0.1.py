from random import shuffle
hearts = [1,2,3,4,5,6,7,8,9,10,10,10,10]
spades = [1,2,3,4,5,6,7,8,9,10,10,10,10]
diamonds = [1,2,3,4,5,6,7,8,9,10,10,10,10]
clubs = [1,2,3,4,5,6,7,8,9,10,10,10,10]
deck = hearts+spades+diamonds+clubs
shuffle(deck)
dealer_hand = [6,1]
player_hand = [1]

def handTotal(hand):
    total = 0
    hand.sort(reverse=True)
    for i in hand:
        if i == 1:
            ace = int(input("You have an ace, do you want it to be an 11 or 1?: "))
            if ace == 11:
                i = 11
        total += i
        print("TOTAL")
        print(total)
    return total

def handPrint(hand):
    hand.sort(reverse = True)
    for i in hand:
        print(i)

def handAdd(hand,deck):
    hand.append(deck[0])
    del deck[0]
    return deck, hand

def totalCheck(player_total, dealer_total):
    if dealer_total > 21:
        print("YOU WIN")
    if player_total == 21:
        print('you win')
    elif dealer_total == 21:
        if player_total == 21:
            print("YOU WIN")
        else:
            print("YOU LOSE")
    elif player_total > dealer_total and (player_total < 21 and dealer_total < 21):
        print("YOU WIN")
    elif player_total == dealer_total:
        print("You win")
    else:
        print("YOU LOSE")


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
handPrint(player_hand)
player_total = handTotal(player_hand)
print('Dealers Hand')
print(dealer_hand[0])
print("?")
while True:
    hit = input("Would you like a new card?(y/n): ").lower()
    if hit == 'y':
        deck, player_hand = handAdd(player_hand, deck)
        print("NEW HAND")
        handPrint(player_hand)
        player_total = handTotal(player_hand)
        if len(player_hand) == 5 and player_total < 21:
            print("FIVE CARDS IN HAND WITHOUT GOING BUST, YOU WIN!!!")
            break
        if player_total > 21:
            print("DEAL HAND")
            handPrint(dealer_hand)
            dealer_total = compHandTotal(dealer_hand, player_total)
            print("DEALER TOTAL")
            print(dealer_total)
            while dealer_total < 17:
                deck, dealer_hand = handAdd(dealer_hand, deck)
                print("NEW DEAL HAND")
                handPrint(dealer_hand)
                dealer_total = compHandTotal(dealer_hand,player_total)
                print("DEALER NEW TOTAL")
                print(dealer_total)
            totalCheck(player_total,dealer_total)
            break
    else:
        print("DEALER HAND")
        handPrint(dealer_hand)
        dealer_total = compHandTotal(dealer_hand,player_total)
        print("DEALER TOTAL")
        print(dealer_total)
        while dealer_total < 17:
            deck, dealer_hand = handAdd(dealer_hand, deck)
            print("NEW DEAL HAND")
            handPrint(dealer_hand)
            dealer_total = compHandTotal(dealer_hand,player_total)
            print("DEALER NEW TOTAL")
            print(dealer_total)
        totalCheck(player_total, dealer_total)
        break
