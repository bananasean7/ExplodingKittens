from random import shuffle
#
class Deck:
    # creating the deck
    def __init__(self, cards = {"Favor": 2, "Skip": 3, "Exploding Kitten": 1, "Attack": 2, "See The Future": 1, 
                                "Nope": 4, "Tacocat": 3, "Beard Cat": 3}):
        self.deck = []
        for item in cards.keys():
            for value in range(0, cards[item]):
                self.deck.append(item)       
        shuffle(self.deck)
    
    def __repr__(self):
        # printing the deck actually prints the deck
        return str(self.deck)

    def shuffle(self):
        # i don't need to explain this
        shuffle(self.deck)
    
    def __getitem__(self, position):
        # allows you to use indices to get values from the deck
        return self.deck[position]

if __name__ == "__main__":
    deck = Deck()
    print(deck)
    print("THIS IS THE WRONG FILE!\nRun explodykittens.py instead!")
