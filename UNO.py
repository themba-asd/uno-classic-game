#UNO Nton Nton
from random import choice, choices, shuffle

colors = ["red", "yellow", "blue", "green"]
deck: list[dict] = [] #{}
bottom_card = any


#create cards and append to the deck array
def create_deck_cards(start, end = 10) -> None:

  for color in colors:
    #
    for number in range(start, end):
      card = {
        "symbol": number,
        "color": color,
      }
      deck.append(card)


#create special cards and append to the deck array
def create_special_deck_cards(rang, symbol) -> None:

  for color in colors:
    #note wilds don't have a specific
    if 'wild' in symbol:
      color = "any"
    #
    for _ in range(rang):
      card = {
        "symbol": symbol,
        "color": color,
      }
      deck.append(card)


#choose  bottom card, remove from deck and return the card
def choose_random_bottom_card() -> dict:

  card: dict = choice(deck)

  #check if its not a special card
  while not str(card.get("symbol")).isnumeric():
    card = choice(deck)
  else:
    deck.remove(card) # remove card from deck
    #bottom_card = card #fix ??
    return card


# this has not been used, do I even need it???,
# maybe for/with played_a_special_card()
def check_bottom_card_is_special() -> tuple[bool, str]:

  symbol = bottom_card.get("symbol")
  if str(symbol).isnumeric():
    return False
  else: return True, symbol


#
def reverse_card_played() -> None:

  pass


#
def skip_card_played() -> None:
  #increment by 2 once
  #if reverse has been played decrement by 2
  #the index of current player
  pass


#
def wild_color_card_played() -> None:
  #set the bottom card symbol and color = color
  #return color
  pass


#
def call_next_player() -> None:
  pass 



###########################################################

#create and shuffle deck
def start_game():

  create_deck_cards(0)  #0-9 cards
  create_deck_cards(1)  #1-9 cards
  create_special_deck_cards(2, "skip")  #skip cards
  create_special_deck_cards(2, "reverse") #reverse cards
  create_special_deck_cards(2, "draw 2")  #draw cards
  create_special_deck_cards(1, "wild color")  #wild cards
  create_special_deck_cards(1, "wild draw 4") #wild draw cards
  shuffle(deck)


###################Class PLAYER########################################

class Player():

  cards: list[dict] = []

  def __init__(self, name = "Player") -> None:

    self.name = name
    self.cards = choices(deck, k=7)

  # 
  def display_player_cards(self): 
    for card in self.cards: print(card)

  #
  def draw_cards(self, number_of_draws) -> None:

    #select random cards from deck and add to player's cards
    cards = choices(deck, k=number_of_draws)
    for card in cards: self.cards.append(card)


    #remove the selected cards from deck
    for card in self.cards: deck.remove(card)


  #check if player has special card
  def player_has_special_card(self) -> bool:

    for card in self.cards:
      symbol = card.get("symbol")
      if type(symbol) == str: return True
    return False


  #show the cards and draw option in ordered list
  def handle_player_options(self):

    counter = 1

    for cards in self.cards:
      print(counter, cards)
      counter += 1
      
    print(counter , "Draw Card")

    user_choice = int(input("Choose a move to play: "))

    #valides the player's choice
    while user_choice > counter + 1:
      user_choice = int(input("You chose an invalid option, try again!"))

    return counter, user_choice


  #
  def play_a_card(self):

    counter, user_choice = self.handle_player_options()

    #last list option will always be to draw cards
    if user_choice == counter:
      self.draw_cards(1)
      print("You chose to draw a card.")
    else:
      player_card = self.cards[user_choice - 1]

      print("You chose: ", player_card)

      #if card played is special, leave this fn & call the played_a_special_card() 
      if type(player_card.get("symbol")) == type(''):
        self.cards.remove(player_card)
        self.played_a_special_card()

      elif bottom_card.get("symbol") == player_card.get("symbol") or bottom_card.get("color") == player_card.get("color") or bottom_card.get("color") == 'any':
        self.cards.remove(player_card)
        print("Correct!")

      else:
        print("Take 2 for your silly mistake! ")
        self.draw_cards(2)
      
    self.display_player_cards()

  def played_a_special_card(self):
    print("Special card played, handling..")
    #I was think match case!!

    pass



######################computer#####################

# class Computer(Player):

#   #if bottom card is a special card, and user has no special card
#   def check_for_next_move():
#     pass


####################################end of class#####################

####################################

start_game()
# FIXXXXXX ????? **** %%%%% #### @@@@@@@
bottom_card = choose_random_bottom_card() #fix, not accessible inside fn??
#bottom_card = {'symbol': "wild", 'color': 'green'}  #choose_random_bottom_card() # fix,  not accessible in fn??

###################################


### net for control ####

# print("bottom card: ", bottom_card)
# print("number of cards: ", len(deck))
# print("deck cards: ")
# for cards in deck: print(cards)
#print("bottom special card: ", check_bottom_card_is_special())


player = Player("frank")
#player2 = Player("tshego")
print("player cards: ", player.name)
#print("player cards: ", player2.name)
#for card in player.cards: print(card)
#print("player has special: ", player.player_has_special_card())


print("bottom card: ", bottom_card)
# print("number of cards: ", len(deck))
# print("deck cards: ")
# for cards in deck: print(cards)
#print("bottom special card: ", check_bottom_card_is_special())

player.play_a_card()
#print("Tshego's turn")
#player2.play_a_card()

