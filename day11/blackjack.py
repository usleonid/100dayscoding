from art import logo
import random
from replit import clear

# def count_scores(list_of_cards):
#   values = ()
#   for card in list_of_cards:
#     card_face = list(card)
#     if card_face[1] == 'J' or card_face[1] == 'Q' or card_face[1] == 'K':
#       score = (10,)
#     elif card_face[1] == 'A':
#       if sum(values) <= 10:
#         score = (11,)
#       else:
#         score = (1,)
#     else:
#       score = (int(card_face[1]),)
#     values += score
#   return sum(values)


def count_scores(list_of_cards):
    values = []
    for card in list_of_cards:
        card_face = list(card)
        if card_face[1] == 'J' or card_face[1] == 'Q' or card_face[1] == 'K':
            score = 10
        elif card_face[1] == 'A':
            if sum(values) <= 10:
                score = 11
            else:
                score = 1
        else:
            score = int(card_face[1])
        values.append(score)
    if 11 in values and sum(values) >= 21:
        values.remove(11)
        values.append(1)
    return sum(values)


def card_issue(list_of_cards):
    card_on_hand = random.choices(card_deck,
                                  weights=None,
                                  cum_weights=None,
                                  k=1)
    list_of_cards.remove(card_on_hand[0])
    return card_on_hand


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
        cards_on_hand += card + ' '
    return cards_on_hand.strip()


suits = {
    'diamonds':
    ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'],
    'hearts':
    ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'],
    'clubs':
    ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'],
    'spades':
    ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'],
}

while True:
    print(logo)

    user_cards = []
    dealer_cards = []
    card_deck = []
    ask_user = 'n'

    # make a deck
    for suit, value in suits.items():
        for rank in value:
            tuple_card = (suit, rank)
            card_deck.append(tuple_card)

    # shuffle a deck
    random.shuffle(card_deck)

    # cards issues
    for i in range(2):
        user_cards.extend(card_issue(card_deck))
        dealer_cards.extend(card_issue(card_deck))

    user_score = count_scores(user_cards)
    dealer_score = count_scores(dealer_cards)

    print(
        f"\n  Your cards: {print_cards_on_hand(user_cards)}, current score: {user_score}"
    )

    print(
        f"  Dealer's first card: {dealer_cards[0][1]}{change_suit(dealer_cards[0][0])}"
    )

    # check blackjack
    if user_score < 21:
        ask_user = input("\nType 'y' to get another card, type 'n' to pass: ")
    else:
        print('You have BlackJack!')
        while dealer_score < 18:
            print(
                f"\n  Dealer's cards on hand: {print_cards_on_hand(dealer_cards)}, current score: {dealer_score}"
            )
            dealer_cards.extend(card_issue(card_deck))
            dealer_score = count_scores(dealer_cards)

        if dealer_score == 21:
            print(
                f"\n  Dealer's final hand: {print_cards_on_hand(dealer_cards)}, current score: {dealer_score}"
            )
            print("It's a draw! 🙃")
            want_to_continue = input(
                "\nDo you want to play one more game of Blackjack? Type 'y' or 'n': "
            )
            if want_to_continue == 'y':
                clear()
                continue
            else:
                break
        else:
            print(
                f"\n  Dealer's final hand: {print_cards_on_hand(dealer_cards)}, current score: {dealer_score}"
            )
            print("You win! \U0001F389")
            want_to_continue = input(
                "\nDo you want to play one more game of Blackjack? Type 'y' or 'n': "
            )
            if want_to_continue == 'y':
                clear()
                continue
            else:
                break

    # continue handling

    while ask_user == 'y':
        user_cards.extend(card_issue(card_deck))
        user_score = count_scores(user_cards)
        print(
            f"\n  Your cards: {print_cards_on_hand(user_cards)}, current score: {user_score}"
        )

        if user_score < 21:
            ask_user = input(
                "\nType 'y' to get another card, type 'n' to pass: ")
        elif user_score > 21:
            print(
                f"\n  Dealer's cards on hand: {print_cards_on_hand(dealer_cards)}, current score: {dealer_score}"
            )
            print('You went over. You lose \U0001F612')
            break
        else:
            print('You have BlackJack!')
            while dealer_score < 18:
                print(
                    f"\n  Dealer's cards on hand: {print_cards_on_hand(dealer_cards)}, current score: {dealer_score}"
                )
                dealer_cards.extend(card_issue(card_deck))
                dealer_score = count_scores(dealer_cards)
            if dealer_score == 21:
                print(
                    f"\n  Dealer's final hand: {print_cards_on_hand(dealer_cards)}, current score: {dealer_score}"
                )
                print("It's a draw! 🙃")
            else:
                print(
                    f"\n  Dealer's final hand: {print_cards_on_hand(dealer_cards)}, current score: {dealer_score}"
                )
                print("You win! \U0001F389")
            break

    while dealer_score < 18 and user_score < 21:
        print(
            f"\n  Dealer's cards on hand: {print_cards_on_hand(dealer_cards)}, current score: {dealer_score}"
        )
        dealer_cards.extend(card_issue(card_deck))
        dealer_score = count_scores(dealer_cards)
    if dealer_score > 21 and user_score < 21:
        print(
            f"\n  Dealer's final hand: {print_cards_on_hand(dealer_cards)}, current score: {dealer_score}"
        )
        print("Opponent went over. You win 😁")
    else:
        if dealer_score > user_score and user_score < 21:
            print(
                f"\n  Dealer's final hand: {print_cards_on_hand(dealer_cards)}, current score: {dealer_score}"
            )
            print("Dealer win! You lose! \U0001F612")
        elif dealer_score == user_score and user_score < 21:
            print(
                f"\n  Dealer's final hand: {print_cards_on_hand(dealer_cards)}, current score: {dealer_score}"
            )
            print("It's a draw! 🙃")
        elif dealer_score < user_score and user_score < 21:
            print(
                f"\n  Dealer's final hand: {print_cards_on_hand(dealer_cards)}, current score: {dealer_score}"
            )
            print("You win! \U0001F389")

    want_to_continue = input(
        "\nDo you want to play one more game of Blackjack? Type 'y' or 'n': ")
    if want_to_continue == 'y':
        clear()
        continue
    else:
        break
