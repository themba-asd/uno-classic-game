#UNO Nton Nton
import random as r

colors = ["red", "yellow", "blue", "green"]
deck: list[dict] = [] #{}
bottom_card = ''


#create cards and append to the deck array
def create_deck_cards(start, end = 10):

  for color in colors:
    #
    for number in range(start, end):
      card = {
        "symbol": number,
        "color": color,
      }
      deck.append(card)


#create special cards and append to the deck array
def create_special_deck_cards(rang, symbol):

  for color in colors:
    #
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

  card: dict = r.choice(deck)

  #check if its not a special card
  while not str(card["symbol"]).isnumeric():
    card = r.choice(deck)
  else:
    deck.remove(card) # remove card from deck
    #bottom_card = card #fix ??
    return card

#shuffle deck and set bottom card
def start_game():

  create_deck_cards(0)  #0-9 cards
  create_deck_cards(1)  #1-9 cards
  create_special_deck_cards(2, "skip")  #skip cards
  create_special_deck_cards(2, "reverse") #reverse cards
  create_special_deck_cards(2, "draw 2")  #draw cards
  create_special_deck_cards(1, "wild")  #wild cards
  create_special_deck_cards(1, "wild draw 4") #wild draw cards
  #r.shuffle(deck)

def check_bottom_card_is_special() -> bool:
  if str(bottom_card["symbol"]).isnumeric():
    return False
  else: return True, bottom_card["symbol"]


##################################
class Player():

  cards: list[dict] = []

  def __init__(self, name) -> None:

    self.name = name


  def draw_cards(self, number_of_draws) -> None:

    #select random cards from deck
    self.cards = r.choices(deck, k=number_of_draws)

    #remove the selected cards from deck
    for card in self.cards:
      deck.remove(card)

  def check_if_can_play(bottom_card) -> bool:

    pass

  def play_a_card():
    pass


####################################
start_game()
bottom_card = {'symbol': "wild", 'color': 'green'}#choose_random_bottom_card() # fix,  not accessible in fn??
###################################


##net for control..

player = Player("frank")
player.draw_cards(5)
print("player cards: ", player.name)
for card in player.cards: print(card)


print("bottom card: ", bottom_card)
# print("number of cards: ", len(deck))
# print("deck cards: ")
# for cards in deck: print(cards)

print(check_bottom_card_is_special())
print(type(check_bottom_card_is_special()))
