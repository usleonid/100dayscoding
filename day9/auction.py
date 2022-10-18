from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

bidding_list = {}
other_bidders = 'Yes'
max_bid = 0
max_bidder = ""

while other_bidders == 'Yes':
  name = input("What is your name?\n")
  bid = int(input("What's your bid?\n$"))
  bidding_list[name] = bid

  other_bidders = input("Are there any other bidders? Type 'Yes' or 'No'.\n")
  clear()

for bidder in bidding_list:
  if bidding_list[bidder] > max_bid:
    max_bid = bidding_list[bidder]
    max_bidder = bidder

print(f"The winner is {max_bidder} with a bid of ${max_bid}.")
