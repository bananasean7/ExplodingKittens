from random import shuffle

class Deck:
    def __init__(self, cards = {"favors": 2, "skips": 3, "exps": 1, "attacks": 2, "stfs": 1, "nopes": 3}):
        self.deck = []
        for item in cards.keys():
            for value in range(0, cards[item]):
                self.deck.append(item)       
        shuffle(self.deck)
    
    def __repr__(self):
        return str(self.deck)

    def shuffle(self):
        shuffle(self.deck)
    
    def __getitem__(self, position):
        return self.deck[position]

if __name__ == "__main__":
    deck = Deck()
    print(deck)
    print("THIS IS THE WRONG FILE!\nRun explodykittens.py instead!")