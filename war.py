def war(player1, player2, pot):

    if len(deck_1) >= 4 and len(deck_2) >= 4:
        remove = deck_1.pop(0)
        pot.append(remove)
        remove = deck_1.pop(0)
        pot.append(remove)
        remove = deck_1.pop(0)
        pot.append(remove)

        remove = deck_2.pop(0)
        pot.append(remove)
        remove = deck_2.pop(0)
        pot.append(remove)
        remove = deck_2.pop(0)
        pot.append(remove)

        remove = deck_1.pop(0)
        pot.append(remove)

        remove = deck_2.pop(0)
        pot.append(remove)

    elif len(deck_1) < 4 or len(deck_2) < 4:
        if len(deck_1) < 4:
            deck_2.extend(deck_1)
            pot.clear()
            deck_1.clear()
        elif len(deck_2) < 4:
            deck_1.extend(deck_2)
            pot.clear()
            deck_2.clear()

    remove = deck_1.pop(0)
    pot.append(remove)
    remove = deck_2.pop(0)
    pot.append(remove)
    print(pot)
    count += 1

    if pot[-2] > pot[-1]:
        remove = pot.pop(0)
        deck_1.append(remove)
        remove = pot.pop(0)
        deck_1.append(remove)

    elif pot[-2] < pot[-1]:
        remove = pot.pop(0)
        deck_2.append(remove)
        remove = pot.pop(0)
        deck_2.append(remove)

    

