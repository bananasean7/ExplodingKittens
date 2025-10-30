from cards import Card

class Player:
    def __init__(self, deck, number):
        self.hand = ["Defuse", "Nope", "Nope", "Skip"]
        self.deck = deck
        self.drawed = False
        self.number = number

    def explode(self):
        if "Defuse" in self.hand:
            self.deck.shuffle()
            self.hand.remove("Defuse")
        else:
            print("THE GAME HAS ENDED.")
            while True:
                pass

    def pickup(self):
        foo = self.deck.deck[0]
        print(f"You have picked up a {foo}")
        if foo == "Exploding Kitten":
            self.explode()
            print("You defuse the Exploding Kitten")
        else:
            self.hand.append(self.deck.deck[0])
            del self.deck.deck[0]


    def take_turn(self, other):
        print(f"It's player {self.number}'s go!")
        if self.drawed == 0:
            self.drawed=1
        while self.drawed != 0:
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
                    card = Card(cardtype, self.deck, self, other)
                    card.played()
                except IndexError or ValueError:
                    print("You can't play that!")
            
            if choice == "S":
                print(self.hand)

if __name__ == "__main__":
    print("THIS IS THE WRONG FILE!\nRun explodykittens.py instead!")