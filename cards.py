from random import choice

class Card:
    def __init__(self, type, deck, player1, player2):
        self.type = type
        self.deck = deck
        self.p1 = player1
        self.p2 = player2
    def favo(self):
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
    
    def attac(self):
        attacklist = ["YOU SUMMON THE GREAT AND ALMIGHTY CATTERWOCKY, DESTROYER OF WORLDS!", "YOU FIRE THE DEVASTATING CRAB-O-PULT",
                        "YOU RELEASE THE TORTURE BUNNIES!"]
        print(choice(attacklist))
        print("The other player must now take two turns!")
        self.p2.drawed = 2
        self.p1.drawed = 0
    
    def st(self):
        stflist = ["You summon the Mantis Shrimp!", "You rub the belly of a Pig-A-Corn!", 
    "You deploy the Special Operations Bunnies!"]
        print(stflist)
        print("You see the future! The next three cards are:")
        print(self.deck[0:3])
    
    def ski(self):
        skiplist = ["You summon the Hypergoat!", "You crab walk with some crabs!", "You fly away on a balloon!"]
        print(choice(skiplist))
        print("You skipped!")
        self.p1.drawed = 0
    
    def check_nope(self, player, other, against): # Player is the one playing the nope, other is the one receiving the nope.
        if player.hand.__contains__("Nope"): # Against is the name of the card being noped.
            nchoice = input(f"Player {player.number}, Would you like to nope the other player's {against}?\nY/N")
            if nchoice == "Y":
                nope_pos = player.hand.index("Nope")
                del player.hand[nope_pos]
                if against != "Nope":
                    foo = other.hand.index(against)
                    del other.hand[foo]
                else:
                    return False
                return True
        return False

    def played(self):
        con = False
        while con == False:
            nope_played = self.check_nope(self.p2, self.p1, self.type)

            if nope_played == False:
                if self.type == "Skip":
                    self.ski()
                
                if self.type == "Favor":
                    self.favo()
                        
                if self.type == "Attack":
                    self.attac()
                
                if self.type == "See The Future":
                    self.st()
                con = True
            else:
                nope_played = self.check_nope(self.p1, self.p2, "Nope")
                if nope_played == True:
                    self.played()
        

if __name__ == "__main__":
    print("THIS IS THE WRONG FILE!\nRun explodykittens.py instead!")

class Cat_Card(Card):
    def __init__(self, type, p1, p2):
        self.type = type
        self.p1 = p1
        self.p2 = p2

    
