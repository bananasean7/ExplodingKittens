from random import shuffle
from player import Player
from deck import Deck
    
def main():
    deck1 = Deck()
    player1 = Player(deck1)
    player2 = Player(deck1)
    while True:
        print("It's Player one's go!")
        player1.take_turn(player2)
        print()
        print("It's Player two's go!")
        player2.take_turn(player1)
    print("THE GAME IS OVER")

if __name__ == "__main__":

    main()
