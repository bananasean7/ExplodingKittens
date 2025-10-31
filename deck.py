from random import shuffle
#
class Deck:
    # creating the deck
    def __init__(self, cards = {"Favor": 4, "Skip": 4, "Exploding Kitten": 2, "Attack": 4, "See The Future": 5, 
                                "Nope": 5, "Tacocat": 4, "Beard Cat": 4, "Rainbow-Ralphing Cat": 4, "Hairy Potato Cat": 4, 
                                "Defuse": 3}):
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
