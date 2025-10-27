from random import shuffle

class Deck:
    def __init__(self, favors=3, skips = 4, exp=2, attacks=3):
        self.deck = []
        self.favors = favors
        self.skips = skips
        self.exps = exp
        self.attacks = attacks
        for favor in range(0,self.favors):
            self.deck.append("Favor")
        for skip in range(0, self.skips):
            self.deck.append("Skip")
        for exploding in range(0,self.exps):
            self.deck.append("Exploding Kitten")
        for attack in range(0, self.attacks):
            self.deck.append("Attack")
        
        shuffle(self.deck)
    
    def __repr__(self):
        return str(self.deck)

    def shuffle(self):
        shuffle(self.deck)