#UNO

colors = ["red", "yellow", "blue", "green"]
wild_cards = ["skip", "reverse", "draw 2", "wild", "wild draw 4"]

deck = [#{
  #   "symbol": "",
  #   "color": "",
  # }
]

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


create_deck_cards(0)  #0-9 cards
create_deck_cards(1)  #1-9 cards

for symbol in wild_cards:
  rang = 2
  if "wild" in symbol: range = 1
  create_special_deck_cards(rang, symbol)

for x in deck: print(x)
