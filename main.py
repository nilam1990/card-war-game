'''
write a program that create card class
card contain suits,rank,value
'''
import random

suits = ("Hearts", "Diamonds", "spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


'''
my_card=Card("Hearts","Four")
print(my_card)

my_card2=Card("Spades","Six")
print(my_card2)

print(" Lets compare two card return smallest value card")

if my_card.value<my_card2.value:
    print(my_card)
else:
    print(my_card2)
'''


class Deck:

    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    # Note this doesn't return anything
    def shuffle(self):
        random.shuffle(self.all_cards)

    # Note we remove one card from the list of all_cards
    def deal_one(self):
        return self.all_cards.pop()


my_deck = Deck()
for card in my_deck.all_cards:
    print(card)
print("After shuffle the cards ")
my_deck.shuffle()
for card in my_deck.all_cards:
    print(card)

my_card = my_deck.deal_one()
print("My Poped card is ")
print(my_card)
print(len(my_deck.all_cards))


class Player:
    def __init__(self, name):
        # new player has name and no any cards
        self.name = name
        self.all_cards = []

    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck

        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)}cards"


'''
my_player=Player("Nilam")
my_player.add_cards(my_card)
my_player.add_cards([my_card,my_card,my_card])
print(my_player)
print("Card rank is "+my_card.rank)
print("Card suit is "+my_card.suit)
print(my_card.value)
'''
# Game Logic

# create two instance of player
player_one = Player("One")
player_two = Player("Two")
# create Deck Object and shuffle the deck
new_deck = Deck()
new_deck.shuffle()

# split the deck between two player
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# check player one has 26 cards or not
print(len(player_one.all_cards))

game_on = True
round_num = 0
while game_on:
    round_num += 1
    print(f" Round {round_num}")
    if len(player_one.all_cards) == 0:
        print("Player one out of Cards! Player Two Wins ..")
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print("Player Two is Out of Cards! Player One Wins..")
        game_on = False
        break
    # start  a New Round
    player_one_cards = []
    player_two_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            # Player One gets the cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            # No Longer at "war" , time for next round
            at_war = False

        elif player_two_cards[-1].value > player_one_cards[-1].value:
            # player Two gets all cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            # No Longer at "war" , time for next round
            at_war = False
        else:
            print("War")
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.

            # First check to see if player has enough cards

            # Check to see if a player is out of cards:

            if len(player_one.all_cards) < 5:
                print("Player one is unable to play the war! Game over at War")
                print("Player Two Wins !!!")
                game_on = False
                break
            if len(player_two.all_cards) < 5:
                print("Player Two is unable to play the war! Game over at War")
                print("Player One Wins !!!")
                game_on = False
                break
            else:
                for i in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())








































































