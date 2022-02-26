import os
clear = lambda: os.system('cls')

from auction_art import logo
print(logo)

bids = {}
bidding_finished = False

def find_hightest_bidder(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"\n\nThe winner is {winner} with a bid of ₹{highest_bid}\n")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: ₹"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if should_continue == "no":
    find_hightest_bidder(bids)
    bidding_finished = True
  elif should_continue == "yes":
    clear()