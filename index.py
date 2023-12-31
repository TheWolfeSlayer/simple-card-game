import random
import os

class Card():
  def __init__(self, value, suit):
    self.value = value
    # Sets value of face cards
    if value == 1:
      self.value = 'Ace'
    elif value == 11:
      self.value = 'Jack'
    elif value == 12:
      self.value = 'Queen'
    elif value == 13:
      self.value = 'King'
      
    self.suit = suit
    
    # Adds a color value to the card depending on suit
    if suit == 'Heart' or suit == 'Diamonds':
      self.color = 'Red'
    if suit == 'Clubs' or suit == 'Spades':
      self.color = 'Black'

  #prints the value of the card
  def printCard(self):
    print(self.value, 'of' , self.suit)

# Makes a user with a name and starting money
class User():
  def __init__(self, name, money):
    self.name = name
    self.money = money

def get_card(deckOfCards):
  # Gets a random card out of the deck and assigns it a variable
  card_location = random.randint(1,len(deckOfCards))
  rand_card = deckOfCards[card_location-1]
  # Removes the card from the deck to prevent duplicates
  deckOfCards.remove(rand_card)
  # Returns the random card selected
  return rand_card

def get_users_card(numInput, first_hidden, second_hidden, third_hidden, first_visible, second_visible, third_visible):
  # Lets user select which pair they want to compare
  if numInput == '1':
    test_cards(first_visible, first_hidden)
  elif numInput == '2':
    test_cards(second_visible, second_hidden)
  elif numInput == '3':
    test_cards(third_visible, third_hidden)

def test_cards(visible_card, hidden_card):
  print(f'Comparing {visible_card.value} of {visible_card.suit} with {hidden_card.value} of {hidden_card.suit}')
  # If cards share the same color and number
  if visible_card.value == hidden_card.value and visible_card.color == hidden_card.color:
    new_user.money += 20
    print(f'Cards are the same color and suit(+$20), player now has {new_user.money}')
  # If cards share the same number
  elif visible_card.value == hidden_card.value:
    new_user.money += 10
    print(f'Cards are the same number(+$10), player now has {new_user.money}')
  # If cards share the same suit
  elif visible_card.suit == hidden_card.suit:
    new_user.money += 5
    print(f'Cards are the same suit(+$5), player now has {new_user.money}')
  # If cards share the same color
  elif visible_card.color == hidden_card.color:
    new_user.money += 1
    print(f'Cards are the same color($+1), player now has {new_user.money}')
  # If there is nothing in common between the two cards
  else:
    print(f'You won nothing! You still have {new_user.money}')

def start_game():
  os.system('cls')
  # Charges user $2 for playing the game
  new_user.money -=2

  # Uses base deck to build temp deck for functions
  temp_deck = base_deck

  # Gets 6 random cards from temp deck
  first_hidden_card = get_card(temp_deck)
  second_hidden_card = get_card(temp_deck)
  third_hidden_card = get_card(temp_deck)
  first_visible_card = get_card(temp_deck)
  second_visible_card = get_card(temp_deck)
  third_visible_card = get_card(temp_deck)

  # Shows the player 3 cards to pick from
  first_visible_card.printCard()
  second_visible_card.printCard()
  third_visible_card.printCard()

  # Player picks a card
  user_input = input('Pick a card by entering 1, 2 or 3\n')
  get_users_card(user_input, first_hidden_card, second_hidden_card, third_hidden_card, first_visible_card, second_visible_card, third_visible_card)
  do_continue()
    
def do_continue():  
  # If the player still has more than $2 remaining, askes them if they want to continue playing
  if new_user.money > 2:
    user_continue = input(f'You have ${new_user.money}, do you want to continue for another $2(-$2)?\n')
    # If yes plays again, if no then ends the program
    if user_continue.lower() == 'Yes':
      new_user.money -=2
      start_game()
    elif user_continue.lower() == 'No':
      print(f'Ending game with ${new_user.money}')
      exit()
    else:
      print('invalid input')
      start_game()
  else:
    print('User has ran out of money, ending game')
    exit()

suits = ['Heart', 'Clubs', 'Diamonds', 'Spades']
# Makes base deck
base_deck = [Card(value, suit) for value in range(1, 14) for suit in suits]
# Asks player for name, makes User class
get_name = input('Enter your name\n')
new_user = User(get_name, 500)

# Asks Player if they want to gamble
yes_or_no = input(f'You have ${new_user.money}, do you want to play a game for $2(-$2)?\n')
if yes_or_no.lower() == 'no':
  print('closing game')
  exit()
elif yes_or_no.lower() == 'yes':
  start_game()
else:
  print('invalid input, closing game')
