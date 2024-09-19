#UNO

colors = ["red", "yellow", "blue", "green"]

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
create_special_deck_cards(2, "skip")  #skip cards
create_special_deck_cards(2, "reverse") #reverse cards
create_special_deck_cards(2, "draw 2")  #draw cards
create_special_deck_cards(1, "wild")  #wild cards
create_special_deck_cards(1, "wild draw 4") #wild draw cards

for x in deck: print(x)
