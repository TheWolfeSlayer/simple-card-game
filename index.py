import random
import os

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

class User():
    def __init__(self, name, money):
        self.name = name
        self.money = money

def get_card(deckOfCards):
    card_location = random.randint(1,len(deckOfCards))
    rand_card = deckOfCards[card_location-1]
    deckOfCards.remove(rand_card)
    return rand_card

def get_users_card(numInput, first_hidden, second_hidden, third_hidden, first_visible, second_visible, third_visible):
    if numInput == '1':
        test_cards(first_visible, first_hidden)
    elif numInput == '2':
        test_cards(second_visible, second_hidden)
    elif numInput == '3':
        test_cards(third_visible, third_hidden)

def test_cards(visible_card, hidden_card):
    print(f'Comparing {visible_card.value} of {visible_card.suit} with {hidden_card.value} of {hidden_card.suit}')
    if visible_card.value == hidden_card.value and visible_card.color == hidden_card.color:
        new_user.money += 20
        print(f'Cards are the same color and suit(+20), player now has {new_user.money}')
    elif visible_card.value == hidden_card.value:
        new_user.money += 10
        print(f'Cards are the same number(+$10), player now has {new_user.money}')
    elif visible_card.suit == hidden_card.suit:
        new_user.money += 5
        print(f'Cards are the same suit(+$5), player now has {new_user.money}')
    elif visible_card.color == hidden_card.color:
        new_user.money += 1
        print(f'Cards are the same color($+1), player now has {new_user.money}')
    else:
        print(f'You won nothing! You still have {new_user.money}')

def start_game():
    os.system('cls')
    new_user.money -=2
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
    get_users_card(user_input, first_hidden_card, second_hidden_card, third_hidden_card, first_visible_card, second_visible_card, third_visible_card)
    do_continue()
    
def do_continue():  
    if new_user.money > 2:
        
        user_continue = input(f'You have ${new_user.money}, do you want to continue for another $2?')
        if user_continue.lower() == 'Yes':
            new_user.money -=2
            start_game()
        elif user_continue.lower() == 'No':
            lets_play_a_game = False
            print(f'Ending game with ${new_user.money}')
            exit()
        else:
            print('invalid input')
            start_game()
    else:
        print('User has ran out of money, ending game')
        lets_play_a_game = False
        exit()

lets_play_a_game = True
suits = ['Heart', 'Clubs', 'Diamonds', 'Spades']
base_deck = [Card(value, suit) for value in range(1, 14) for suit in suits]
get_name = input('Enter your name')
new_user = User(get_name, 500)


yes_or_no = input(f'You have ${new_user.money}, do you want to play a game for $2?')
if yes_or_no.lower() == 'no':
    print('Ending game')
    exit()
while lets_play_a_game == True:
    start_game()