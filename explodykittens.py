from random import shuffle
from player import Player
from deck import Deck
    
def main():
    deck1 = Deck()
    player1 = Player(deck1, 1)
    player2 = Player(deck1, 2)
    print()
    while True:
        player1.take_turn(player2)
        player2.take_turn(player1)
    print("THE GAME IS OVER") # It'll be a long time before this function runs lol

if __name__ == "__main__":
    main()
    