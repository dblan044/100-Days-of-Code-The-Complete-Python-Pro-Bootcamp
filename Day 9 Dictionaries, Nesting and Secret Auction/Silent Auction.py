import art
# TODO-1: Ask the user for input
print(art.logo)
print("Welcome to the secret auction!")

# TODO-4: Compare bids in dictionary
def highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")

name_and_bid = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    # TODO-2: Save data into dictionary {name: price}
    name_and_bid[name] = bid

    # TODO-3: Whether if new bids need to be added
    should_continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue_bidding == "yes":
        print("\n" * 25)

    if should_continue_bidding == "no":
        continue_bidding = False
        highest_bidder(name_and_bid)
