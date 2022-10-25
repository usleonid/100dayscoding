def change_suit(suit):
  if suit == 'diamonds':
    suit_picture = "\U00002666"
  elif suit == 'hearts':
    suit_picture = "\U00002665"
  elif suit == 'clubs':
    suit_picture = "\U00002663"
  elif suit == 'spades':
    suit_picture = "\U00002660"
  return suit_picture
    
def print_cards_on_hand(list_of_cards):
  cards_on_hand = str()
  card = str()
  for i in range(len(list_of_cards)):
    card = list_of_cards[i][1] + change_suit(list_of_cards[i][0])
    cards_on_hand += card+' ' 
  return cards_on_hand.strip()

    
user_cards = [('clubs', '10'), ('hearts', 'K')]

print(f"  Your cards: {print_cards_on_hand(user_cards)}")