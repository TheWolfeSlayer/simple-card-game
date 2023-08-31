import random

class Card():
    def __init__(self, value, suit):
        self.value = value
        if value == 1:
            self.value = 'Ace'
        elif value == 11:
            self.value = 'Jack'
        elif value == 12:
            self.value = 'Queen'
        elif value == 13:
            self.value = 'King'
        self.suit = suit
        if suit == 'Heart' or suit == 'Diamonds':
            self.color = 'Red'
        if suit == 'Clubs' or suit == 'Spades':
            self.color = 'Black'

    def printCard(self):
        print(self.value, 'of' , self.suit)

def get_card(deckOfCards):
    card_location = random.randint(0,len(deckOfCards))
    rand_card = deckOfCards[card_location]
    deckOfCards.remove(rand_card)
    return rand_card

def get_users_card(numInput):
    if numInput == '1':
        test_cards(first_visible_card, first_hidden_card)
    elif numInput == '2':
        test_cards(second_visible_card, second_hidden_card)
    elif numInput == '3':
        test_cards(third_visible_card, third_hidden_card)

def test_cards(visible_card, hidden_card):
    print(f'Comparing {visible_card.value} of {visible_card.suit} with {hidden_card.value} of {hidden_card.suit}')
    if visible_card.value == hidden_card.value and visible_card.color == hidden_card.color:
        print('SAME COLOR AND NUMBER')
    elif visible_card.value == hidden_card.value:
        print('SAME NUMBER')
    elif visible_card.suit == hidden_card.suit:
        print('SAME SUIT')
    elif visible_card.color == hidden_card.color:
        print('SAME COLOR')


suits = ['Heart', 'Clubs', 'Diamonds', 'Spades']

base_deck = [Card(value, suit) for value in range(1, 14) for suit in suits]

temp_deck = base_deck
first_hidden_card = get_card(temp_deck)
second_hidden_card = get_card(temp_deck)
third_hidden_card = get_card(temp_deck)
first_visible_card = get_card(temp_deck)
second_visible_card = get_card(temp_deck)
third_visible_card = get_card(temp_deck)


first_visible_card.printCard()
second_visible_card.printCard()
third_visible_card.printCard()
user_input = input('Pick a card by entering 1, 2 or 3\n')
get_users_card(user_input)