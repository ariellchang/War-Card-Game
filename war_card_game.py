# War Card Game

import random
import player

cards = []
file = open('deck_b.txt', 'r')
for line in file:
    cards.append(line.strip())

for i in range(0, len(cards)):
    cards[i] = int(cards[i])

# Input Both Player's Name
player_1_name = input("Enter player 1's name: ")
player_2_name = input("Enter player 2's name: ")

# Player Instances
player1 = player.Player(player_1_name)
player2 = player.Player(player_2_name)

deck_1 = player1.deck
deck_2 = player2.deck
pot = []

for i in range(0, len(cards)-1, 2):
    deck_1.append(cards[i])
    deck_2.append(cards[i+1])

# Game Play
def battle(pot):
    pot.append(deck_1.pop(0))
    pot.append(deck_1.pop(0))
    pot.append(deck_1.pop(0))

    pot.append(deck_2.pop(0))
    pot.append(deck_2.pop(0))
    pot.append(deck_2.pop(0))

    pot.append(deck_1.pop(0))
    pot.append(deck_2.pop(0))

       # remove = deck_1.pop(0)
       # pot.append(remove)
       # remove = deck_1.pop(0)
       # pot.append(remove)
       # remove = deck_1.pop(0)
       # pot.append(remove)

       # remove = deck_2.pop(0)
       # pot.append(remove)
       # remove = deck_2.pop(0)
       # pot.append(remove)
       # remove = deck_2.pop(0)
       # pot.append(remove)

       # remove = deck_1.pop(0)
       # pot.append(remove)

       # remove = deck_2.pop(0)
       # pot.append(remove)

    if pot[-2] > pot[-1]:
        deck_1.extend(pot)
        pot.clear()
        return
        # remove = pot.pop(0)
        # deck_1.append(remove)
        # remove = pot.pop(0)
        # deck_1.append(remove)

    elif pot[-2] < pot[-1]:
        deck_2.extend(pot)
        pot.clear()
        return
        # remove = pot.pop(0)
        # deck_2.append(remove)
        # remove = pot.pop(0)
        # deck_2.append(remove)

    elif pot[-2] == pot[-1]:
        if len(deck_1) < 4:
            deck_2.extend(pot)
            deck_2.extend(deck_1)
            pot.clear()
            deck_1.clear()
            return
        elif len(deck_2) < 4:
            deck_1.extend(pot)
            deck_1.extend(deck_2)
            pot.clear()
            deck_2.clear()
            return
        else:
            battle(pot)
            return

# Main
count = 0
while deck_1 and deck_2:

    while len(deck_1) != 0 and len(deck_2) != 0:

        pot.append(deck_1.pop(0))
        pot.append(deck_2.pop(0))
        # remove = deck_1.pop(0)
        # pot.append(remove)
        # remove = deck_2.pop(0)
        # pot.append(remove)
        count += 1
        print(deck_1)
        print(deck_2)
        print(pot)

        if pot[-2] > pot[-1]:
            deck_1.extend(pot)
            pot.clear()
            # remove = pot.pop(0)
            # deck_1.append(remove)
            # remove = pot.pop(0)
            # deck_1.append(remove)

        elif pot[-2] < pot[-1]:
            deck_2.extend(pot)
            pot.clear()
            # remove = pot.pop(0)
            # deck_2.append(remove)
            # remove = pot.pop(0)
            # deck_2.append(remove)

        else:
            if len(deck_1) < 4:
                deck_2.extend(pot)
                deck_2.extend(deck_1)
                pot.clear()
                deck_1.clear()
                break
            elif len(deck_2) < 4:
                deck_1.extend(pot)
                deck_1.extend(deck_2)
                pot.clear()
                deck_2.clear()
                break
            else:
                battle(pot)
                break

# Print Winner
    if len(deck_1) == 0:
        print("Player {} won in {} rounds.".format(player_2_name, count))
    elif len(deck_2) == 0:
        print("Player {} won in {} rounds.".format(player_1_name, count))
