# make a deck of playing cards

import random

card_faces = []
suits = ["Hearts","Diamonds","Spades","Clubs"]
royals = ["King", "Queen", "Joker", "Ace"]
deck = []

for i in range(2,11):
    card_faces.append(str(i))

for j in range(4):
    card_faces.append(royals[j])

# print(card_faces)

# attach suits
for k in range(4):
    for l in range(13):
        card = (card_faces[l] + " of "+suits[k])
        deck.append(card)

# all 52 cards

for m in range(52):
    print(deck[m])
