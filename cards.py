from random import choice

class Card:
    def __init__(self, type):
        self.type = type

    def played(self, player, other):
        if self.type == "Skip":
            skiplist = ["You summon the Hypergoat!", "You crab walk with some crabs!", "You fly away on a balloon!"]
            print(choice(skiplist))
            print("You skipped!")
            player.drawed = 0
        
        if self.type == "Favor":
            try:
                taken_card = int(input("(This choice is for the player the card was played against)\nAt what position would you like to give away a card: "))
            except ValueError:
                print("That is not a number!")
                print("Taking the last card...")
                taken_card = -1
                given_card = other.hand[taken_card]
            try:
                given_card = other.hand[taken_card]
            except IndexError or ValueError:
                print("You don't have a card there!")
                print("Taking the last card...")
                taken_card = -1
                given_card = other.hand[taken_card]

            favorlist = ["You rub Peanut Butter on your belly!", "Your send an army of squirrels against your opponent!"]
            print(choice(favorlist))
            print(f"You received a {given_card}")
            del other.hand[taken_card]
            player.hand.append(given_card)
        
        if self.type == "Attack":
            attacklist = ["YOU SUMMON THE GREAT AND ALMIGHTY CATTERWOCKY, DESTROYER OF WORLDS!", "YOU FIRE THE DEVASTATING CRAB-O-PULT",
                          "YOU RELEASE THE TORTURE BUNNIES!"]
            print(choice(attacklist))
            print("Player two must now take two turns!")
            other.drawed = 2
            player.drawed = 0

if __name__ == "__main__":
    print("THIS IS THE WRONG FILE!\nRun explodykittens.py instead!")