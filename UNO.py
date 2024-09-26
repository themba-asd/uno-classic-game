#UNO Nton Nton
from random import choice, choices, shuffle

colors = ["red", "yellow", "blue", "green"]
deck: list[dict] = []
bottom_card: dict[str | int] = any
player_names: list[str] = []
game_players: dict = {}
current_player: int = 0


###################player class
class Player():

  cards: list[dict] = []

  def __init__(self, name = "Player") -> None:
    self.name = name
    self.cards = choices(deck, k=1)


  def check_if_winner(self) -> None:
    if len(self.cards) < 1:
      exit(f"\n -------- WE HAVE A WINNER-----: {self.name} -- WON!!!--------")


  def display_player_cards(self) -> None: 

    print(f"\nBottom Card: {bottom_card} \n\n These Are {self.name}'s Cards: ")
    
    counter = 0

    for card in self.cards:
      counter += 1
      print(" ", counter, card)

    print(" ", counter + 1, "Draw Card")


  def draw_cards(self, number_of_draws: int) -> None:

    #select random cards from deck and add to player's cards
    cards = choices(deck, k=number_of_draws)
    for card in cards: self.cards.append(card)


  #show the cards and draw option in ordered list
  def handle_player_options(self) -> tuple:

    counter = len(self.cards) + 1

    self.display_player_cards()

    user_choice = input("\nChoose a move to play: ")

    #valides the player's choice
    while not user_choice.isdigit() or int(user_choice) > counter or user_choice == '0':
      user_choice = input("Invalid option, choose again: ")

    return counter, int(user_choice)

  #
  def play_a_card(self) -> None:

    print(f"\n -----------------------------\n{self.name} is now playing.")

    counter, user_choice = self.handle_player_options()

    #last list option will always be to draw cards
    if user_choice == counter:
      self.draw_cards(1)
      print(f"\n Player Chose To Draw A Card.")
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

      else:
        self.draw_cards(2)
        print("\nTake +2 for your careless mistake! Nxa!")
      
    self.check_if_winner()

  #
  def played_a_special_card(self, card: dict) -> None:

    card_symbol = card.get("symbol")

    match card_symbol:

        case 'wild color':
            change_bottom_card(card)
            print("\nAny Color Can Be Played!")

        case 'skip':
            skip_card_played()
            change_bottom_card(card)
            print(f"\nSkipped Player {(game_players.get(player_names[current_player + 1])).name}")

        case 'reverse':
            handle_reverse_fn()
            print("\nDirection Reversed, Hade Mfethu")
            
        case "draw 2":
            draw_card_played(2)
            change_bottom_card(card)

        case "wild draw 4":
            draw_card_played(4)
            change_bottom_card(card)
            
    change_bottom_card(card)


######################computer classs
class Computer(Player):

 def handle_player_options(self) -> tuple:

    counter = len(self.cards) + 1
    user_choice = 1

    self.display_player_cards()

    for card in self.cards:
      if card.get("symbol") == bottom_card.get("symbol") or card.get("color") == bottom_card.get("color") or "wild" in str(card.get("symbol")) or "wild" in str(bottom_card.get("symbol")):
        return counter, user_choice
      user_choice += 1
    else: return counter, counter

  #
def play_a_card(self) -> None:

  print(f"\n{self.name} is now playing.")

  counter, user_choice = self.handle_player_options()
  #last list option will always be to draw cards
  if user_choice == counter:
    self.draw_cards(1)
    print(f"\n{self.name} chose to draw a card.")
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

    else:
      self.draw_cards(2)
      print("\nTake +2 for your careless mistake! Nxa!")

  self.check_if_winner()

####################################end of class

#create cards and append to the deck array
def create_deck_cards(start: int, end: int = 10) -> None:

  for color in colors:
    #
    for number in range(start, end):
      card = {
        "symbol": number,
        "color": color,
      }
      deck.append(card)


#create special cards and append to the deck array
def create_special_deck_cards(rang: int, symbol: str) -> None:

  for color in colors:
    #note wilds don't have a specific
    if 'wild' in symbol:
      color = "any"
    #
    for _ in range(rang):
      card = {
        "symbol": symbol, "color": color,
      }
      deck.append(card)

#
def change_bottom_card(card: dict) -> None:
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
    deck.remove(card)
    return card

#
def reverse_card_played() -> list[str]:
  
  global current_player
  player_names_reversed = []
  index = current_player - 1
  
  for _ in range(len(player_names)):
    player_names_reversed.append(player_names[index])
    index -= 1

  return player_names_reversed

#
def handle_reverse_fn() -> None:
  
  global current_player
  
  x = reverse_card_played()
  player_names.clear()
  player_names.extend(x)
  current_player = 0

#
def skip_card_played() -> None:

  global current_player
  current_player += 1

#
def draw_card_played(number: int) -> None:
  
  global current_player
  
  target_player_index = current_player + 1
  
  target_player = (game_players.get(player_names[target_player_index]))

  target_player.draw_cards(number)
  
  skip_card_played()
  
  print(f"{number} Shots Fired!!: {target_player.name} Take + {number} Then Fight Back")

#create and shuffle deck
def start_game():

  create_deck_cards(0)  #0-9 cards
  create_deck_cards(1)  #1-9 cards
  create_special_deck_cards(2, "skip")  #skip cards
  create_special_deck_cards(2, "reverse") #reverse cards
  create_special_deck_cards(2, "draw 2")  #draw cards
  create_special_deck_cards(1, "wild color")  #wild cards
  create_special_deck_cards(1, "wild draw 4") #wild draw cards
  change_bottom_card(set_random_bottom_card())
  shuffle(deck)


def create_players() -> None:

  counter = 1
  number_of_players = int(input("Enter number of human players: "))

  for _ in range(number_of_players):
    name = input(f"Enter Player {counter} Username: ")
    player_names.append(name)
    counter += 1
  
  handle_players(player_names)

#
def handle_players(player_names: list) -> dict:

  global game_players

  for name in player_names:
      game_players[name] = Player(name)
  #Computer Players
  player_names.append("Computer")
  game_players["Computer"] = Computer("Computer")

  print(f"\nPlayers: ", end=" ")
  for name in player_names: 
    print(f"| {name} ", end=" ")

  return game_players

#
def call_player() -> None:

  global current_player

  if current_player >= len(player_names):
    current_player = 0
  if current_player < len(player_names):
    (game_players.get(player_names[current_player])).play_a_card()
    current_player += 1

  call_player()

######################It All Starts Here
start_game()
create_players()
call_player()
