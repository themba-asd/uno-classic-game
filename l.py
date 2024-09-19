#UNO

colors = ["red", "yellow", "blue", "green"]

deck = [
  # {
  #   "symbol": "",
  #   "color": "",
  # }
]

for color in colors:
  #0-9 cards
  for i in range(10):
    card = {
      "symbol": i,
      "color": color,
    }
    deck.append(card)

  #1-9 cards
  for i in range(1,10):
    card = {
      "symbol": i,
      "color": color,
    }
    deck.append(card)

  #skip cards
  for _ in range(2):
    card = {
      "symbol": "skip",
      "color": color,
    }
    deck.append(card)

  #reverse cards
  for _ in range(2):
    card = {
      "symbol": "reverse",
      "color": color,
    }
    deck.append(card)

  #draw cards
  for _ in range(2):
    card = {
      "symbol": "draw 2",
      "color": color,
    }
    deck.append(card)

  #wild cards
  for _ in range(1):
    card = {
      "symbol": "wild",
      "color": "any",
    }
    deck.append(card)

  #wild draw cards
  for _ in range(1):
    card = {
      "symbol": "wild draw 4",
      "color": "any",
    }
    deck.append(card)


for x in deck: print(x)

