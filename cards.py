class Card:
    def __init__(self, type):
        self.type = type

    def played(self, player, other):
        if self.type == "Skip":
            print("You skipped!")
            player.drawed = True
        
        if self.type == "Favor":
            taken_card = int(input("(This choice is for the player the card was played against)\nAt what position would you like to give away a card: "))
            given_card = other.hand[taken_card]
            print(f"You received a {given_card}")
            del other.hand[taken_card]
            player.hand.append(given_card)