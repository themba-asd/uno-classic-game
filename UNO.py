#UNO Nton Nton
from random import choice, choices, shuffle

colors = ["red", "yellow", "blue", "green"]
deck: list[dict] = [] #{}
bottom_card: dict = any


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


#fix this thing???
#change bottom card
def change_bottom_card(card) -> None:
  global bottom_card 
  bottom_card = card
  

#choose  bottom card, remove from deck and return the card
def set_random_bottom_card() -> dict:

  card: dict = choice(deck)

  #check if its not a special card
  while not str(card.get("symbol")).isnumeric():
    card = choice(deck)
  else:
    change_bottom_card(card)
    deck.remove(card) # remove card from deck
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
def draw_2_card_played() -> None:
  #set the bottom card symbol and color = color
  #return color

  pass


#
def wild_draw_card_played() -> None:
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
  def display_player_cards(self) -> None: 

    print("\nBottom Card: ", bottom_card, "\n")
    
    counter = 0

    for cards in self.cards:
      counter += 1
      print(counter, cards)


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
  def handle_player_options(self) -> tuple:

    counter = len(self.cards) + 1

    self.display_player_cards()
      
    print(counter , "Draw Card")

    user_choice = input("\nChoose a move to play: ")

    #valides the player's choice
    while not user_choice.isdigit() or int(user_choice) > counter or user_choice == '0':
      user_choice = input("Invalid option, choose again: ")

    return counter, int(user_choice)


  #
  def play_a_card(self) -> None:

    counter, user_choice = self.handle_player_options()

    #last list option will always be to draw cards
    if user_choice == counter:
      self.draw_cards(1)
      print("You chose to draw a card.")
    else:
      player_card = self.cards[user_choice - 1]

      print("Card Played: ", player_card)

      #validate card played
      if bottom_card.get("symbol") == player_card.get("symbol") or bottom_card.get("color") == player_card.get("color") or bottom_card.get("color") == 'any' or player_card.get("color") == 'any':
      #if card played is special, leave this fn & call the played_a_special_card() 
        if type(player_card.get("symbol")) == type(''):
          self.played_a_special_card(player_card)
          self.cards.remove(player_card)
        else:
          change_bottom_card(player_card)
          self.cards.remove(player_card)
          print("Correct, Next Player Please")

      else:
        print("\nTake +2 for your careless mistake! Nxa!")
        self.draw_cards(2)
      
    self.display_player_cards()

  def played_a_special_card(self, card) -> None:

    print("\nSpecial card played, handling..")

  # "skip"  4x2 skip cards
  # "reverse" 4x2 reverse cards
  # "draw 2"   4x2 draw cards
  # "wild color"  4x wild cards, any color
  # "wild draw 4" 4x wild draw cards, any color

    card_symbol = card.get("symbol")

    match card_symbol:
        
        case 'wild color':
            change_bottom_card(card)
            #call next player
            print("\nAny Color Can Be Played!")

        case 'skip':
            skip_card_played()
            change_bottom_card(card)
            print("\nSkipped Next Player, Askies")

        case 'reverse':
            reverse_card_played()
            print("\nDirection Reversed, Hade Mfethu")

        case "draw 2":
            draw_2_card_played()
            change_bottom_card(card)
            print("\nTake +2 Baba")

        # default pattern
        case "wild draw 4":
            wild_draw_card_played()
            change_bottom_card(card)
            print("\nTake +4 or Fight Back?, Any Color!")

    #self.cards.remove(card)



######################computer#####################

# class Computer(Player):

#   #if bottom card is a special card, and user has no special card
#   def check_for_next_move():
#     pass


####################################end of class#####################

####################################

start_game()
bottom_card = set_random_bottom_card()
#bottom_card = {'symbol': "wild", 'color': 'green'}

###################################


### net for control ####

# print("bottom card: ", bottom_card)
# print("number of cards: ", len(deck))
# print("deck cards: ")
# for cards in deck: print(cards)
#print("bottom special card: ", check_bottom_card_is_special())


player = Player("Frank Franklin")
#player2 = Player("tshego")
print("Player Name: ", player.name)
#print("player cards: ", player2.name)
#for card in player.cards: print(card)
#print("player has special: ", player.player_has_special_card())


#print("bottom card: ", bottom_card)
# print("number of cards: ", len(deck))
# print("deck cards: ")
# for cards in deck: print(cards)
#print("bottom special card: ", check_bottom_card_is_special())

player.play_a_card()
#print("Tshego's turn")
#player2.play_a_card()

