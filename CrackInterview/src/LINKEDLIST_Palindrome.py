from random import shuffle    
class Card:
    def __init__(self,suit,num):
        self.suit = suit
        self.num = num

deck = list()
suits = ['Diamond', 'Heart', 'Spade', 'Club']

nums = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

for suit in suits: #This is the code that actually makes a deck
    for num in nums:
        deck.append(Card(suit,num))

shuffle(deck)
for number in range(13):
    for player in range(4):
        #deal cards here using deck.pop()
        print(deck.pop().num) #just to prove it works randomly =P   