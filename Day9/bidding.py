from replit import clear
from art import logo    

print(logo)

bid = {}

bidding = True
while bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bid[name] = price
    more = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more == "no":
        bidding = False
        highest_bid = 0
        winner = ""
        for bidder in bid:
            if bid[bidder] > highest_bid:
                highest_bid = bid[bidder]
                winner = bidder
        print(f"The winner is {winner} with a bid of ${highest_bid}.")
    elif more == "yes":
        clear()
        