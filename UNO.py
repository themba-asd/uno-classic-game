#UNO Nton Nton
import random as r

colors = ["red", "yellow", "blue", "green"]
deck: list[dict] = [] #{}

bottom_card = ''

def create_deck_cards(start, end = 10):

  for color in colors:
    #
    for i in range(start, end):
      card = {
        "symbol": i,
        "color": color,
      }
      deck.append(card)


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

#choose bottom card, remove from deck and return the card
def choose_random_bottom_card():
  card = r.choice(deck)
  #check if its not a special card
  while not str(card["symbol"]).isnumeric():
    card = r.choice(deck)
  else:
    deck.remove(card)
    return card

#shuffle deck and set bottom card
def start_game():
  #r.shuffle(deck)
  pass


#Net for control
#for x in deck: print(x)

create_deck_cards(0)  #0-9 cards
create_deck_cards(1)  #1-9 cards
create_special_deck_cards(2, "skip")  #skip cards
create_special_deck_cards(2, "reverse") #reverse cards
create_special_deck_cards(2, "draw 2")  #draw cards
create_special_deck_cards(1, "wild")  #wild cards
create_special_deck_cards(1, "wild draw 4") #wild draw cards

# remember it's not accessed in fn(start fn)??? fixx, 
bottom_card = choose_random_bottom_card()








#net for control..
start_game()
print(bottom_card)
print("xxxxx")
for x in deck: print(x)
