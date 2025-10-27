from cards import Card

class Player:
    def __init__(self, deck):
        self.hand = ["Defuse"]
        self.deck = deck
        self.drawed = False

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
        if foo == "Exploding Kitten":
            self.explode()
            print("You defuse the Exploding Kitten")
        else:
            self.hand.append(self.deck.deck[0])
            del self.deck.deck[0]
        return foo

    def take_turn(self, other):
        self.drawed=False
        while self.drawed == False:
            choice = input("Would you like to Play, See hand or Draw?\nP/S/D: ")
            if choice == "D":
                bar = self.pickup()
                print(f"You picked up a {bar}!")
                self.drawed=True
            if choice == "P":
                playchoice = int(input("At what position is the card you wish to play?"))
                cardtype = self.hand[playchoice]
                card = Card(cardtype)
                card.played(self, other)
            if choice == "S":
                print(self.hand)