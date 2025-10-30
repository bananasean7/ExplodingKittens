from cards import Card
from cards import Cat_Card

class Player:
    def __init__(self, deck, number):
        # setting up player
        self.hand = ["Defuse", "Tacocat", "Tacocat"]
        self.deck = deck
        self.drawed = False
        self.number = number
        self.catlist = ["Tacocat", "Beard Cat"]

    def explode(self):
        # explains itself
        if "Defuse" in self.hand:
            self.deck.shuffle()
            self.hand.remove("Defuse")
        else:
            print("THE GAME HAS ENDED.")
            while True:
                pass

    def pickup(self):
        # picking up cards
        foo = self.deck.deck[0]
        print(f"You have picked up a {foo}")
        if foo == "Exploding Kitten":
            self.explode()
            print("You defuse the Exploding Kitten")
        else:
            # append the first item of the deck, then delete it using the __getitem__
            self.hand.append(self.deck.deck[0])
            del self.deck.deck[0]


    def take_turn(self, other):
        # start of turn
        print(f"It's player {self.number}'s go!")
        if self.drawed == 0:
            # has not drawn
            self.drawed=1
        while self.drawed != 0:
            # while player hasn't drawn
            print()
            choice = input(f"Player {self.number}, Would you like to Play, See hand or Draw?\nP/S/D: ")
            if choice == "D":
                self.pickup()
                self.drawed-=1

            if choice == "P":
                print(self.hand)
                try:
                    playchoice = int(input("At what position is the card you wish to play?  "))
                    cardtype = self.hand[playchoice]
                    if not cardtype in self.catlist:
                        card = Card(cardtype, self.deck, self, other)
                        card.played()
                    else:
                        card = Cat_Card(cardtype, self.deck, self, other)
                        card.played()
                except IndexError or ValueError:
                    print("You can't play that!")
            
            if choice == "S":
                print(self.hand)

if __name__ == "__main__":
    print("THIS IS THE WRONG FILE!\nRun explodykittens.py instead!")