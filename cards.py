from random import choice

class Card:
    def __init__(self, type, deck, player1, player2):
        self.type = type
        self.deck = deck
        self.p1 = player1
        self.p2 = player2
    
    def favor(self):
        try:
            print(self.p2.hand)
            taken_card = int(input("(This choice is for the player the card was played against)\nAt what position would you like to give away a card: "))
        except ValueError:
            print("That is not a number!")
            print("Taking the last card...")
            taken_card = -1
            given_card = self.p2.hand[taken_card]
        try:
            given_card = self.p2.hand[taken_card]
        except IndexError or ValueError:
            print("You don't have a card there!")
            print("Taking the last card...")
            taken_card = -1
            given_card = self.p2.hand[taken_card]

        favorlist = ["You rub Peanut Butter on your belly!", "Your send an army of squirrels against your opponent!"]
        print(choice(favorlist))
        print(f"You received a {given_card}")
        del self.p2.hand[taken_card]
        self.p1.hand.append(given_card)
    
    def attack(self):
        attacklist = ["YOU SUMMON THE GREAT AND ALMIGHTY CATTERWOCKY, DESTROYER OF WORLDS!", "YOU FIRE THE DEVASTATING CRAB-O-PULT",
                        "YOU RELEASE THE TORTURE BUNNIES!"]
        print(choice(attacklist))
        print("The other player must now take two turns!")
        self.p2.drawed = 2
        self.p1.drawed = 0
    
    def stf(self):
        stflist = ["You summon the Mantis Shrimp!", "You rub the belly of a Pig-A-Corn!", 
    "You deploy the Special Operations Bunnies!"]
        print(choice(stflist))
        print("You see the future! The next three cards are:")
        print(self.deck[0:3])
    
    def skip(self):
        skiplist = ["You summon the Hypergoat!", "You crab walk with some crabs!", "You fly away on a balloon!"]
        print(choice(skiplist))
        print("You skipped!")
        self.p1.drawed = 0
    
    def check_nope(self):
        while True:
            if "Nope" in self.p2.hand:
                nchoice = input(f"Player {self.p2.number}, Would you like to play a nope?\nY/N:")
                if nchoice == "Y":
                    nope_pos = self.p2.hand.index("Nope")
                    del self.p2.hand[nope_pos]
                    if "Nope" in self.p1.hand:
                        nchoice = input(f"Player {self.p1.number}, Would you like to nope the nope?\nY/N: ")
                        if nchoice == "Y":
                            nope_pos = self.p1.hand.index("Nope")
                            del self.p1.hand[nope_pos]
                        else:
                            return True
                    else:
                        return True
                else:
                    return False
            else:
                return False


    def played(self):
        nope_played = self.check_nope()

        if nope_played == False:
            if self.type == "Skip":
                self.skip()
            
            if self.type == "Favor":
                self.favor()
                    
            if self.type == "Attack":
                self.attack()
            
            if self.type == "See The Future":
                self.stf()
        
        foo = self.p1.hand.index(self.type)
        self.p1.hand.pop(foo)

class Cat_Card(Card):
    def __init__(self, type, p1, p2, deck):
        self.type = type
        self.deck = deck
        self.p1 = p1
        self.p2 = p2
        super().__init__(type, p1, p2, deck)

    def played(self):
            combochoice = input("Would you like to do \nA: A two of a kind?\nOr\nB: A three of a kind?\nA/B: ")
            if combochoice == "A":
                try:
                    card1_pos = self.p1.hand.index(self.type)
                    card2_pos = self.p1.hand.index(self.type, card1_pos+1)
                    self.p1.hand.pop(card1_pos)
                    self.p1.hand.pop(card2_pos-1)
                    nope_played = super().check_nope()

                    if nope_played == False:
                        print(f"Taking a card from Player {self.p2.number}...")
                        given_card = choice(self.p2.hand)
                        taken_card = self.p2.hand.index(given_card)
                        self.p2.hand.pop(taken_card)
                        self.p1.hand.append(given_card)
                        print(f"A {given_card} has been taken!")
                except ValueError or IndexError:
                    print("You don't have two of the same card or your opponent has an empty hand!")
            

if __name__ == "__main__":
    card = Cat_Card()
    card.played()