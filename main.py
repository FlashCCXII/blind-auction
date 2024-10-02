from replit import clear

from art import logo

print(logo)
print("Welcome to the secret auction program.")
bids = {}
should_continue = True

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while should_continue:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bids[name] = bid
  decision = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if decision != "yes":
    should_continue = False
    find_highest_bidder(bids)
  elif decision == "yes":
    clear()
