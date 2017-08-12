def handTotal(hand):
    hand.sort(reverse=True)
    for i in hand:
        print(i)
        if i == 1:
            ace = int(input("You have an ace, do you want it to be an 11 or 1?: "))
            if ace == 11:
                print(i)
        total += i
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





def compHandTotal(hand):
    ptotal = handTotal(phand)

    total = 0
    hand.sort(reverse=True)
    for i in hand:
        if i == 1:
            total1 = total + 1
            total11 = total + 11
            if total1 < 21 and total11 > 21:
                i = 11
            elif total11 > ptotal and total11 < 21:
                i = 11
            else:
                i = 1

        total += i
    return total