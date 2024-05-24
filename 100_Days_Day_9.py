##################
# Silent Auction #
##################

print("Welcome to the secret auction program.\n")

# Empty dictionary of bidders and bids.
bidders_bids_dictionary = {}

# The "while" loop that is the actual auction process.
continue_bidding = True
while continue_bidding == True:
    # The bidder will be the key.
    bidder = str(input("What is your name?\n"))
    print(bidder) # TEST CODE

    # The bid will be the value.
    bid = int(input("What is your bid?\n"))
    print(bid) # TEST CODE

    # Putting the key and value together in the dictionary.
    bidders_bids_dictionary[bidder] = bid
    print(bidders_bids_dictionary) # TEST CODE

    # Offering the chance for other bidders before finishing the auction.
    done_bidding = str(input("Are there any other bidders?  Type \"yes\" or \"no\": ").lower())
    if done_bidding == "no":
        continue_bidding = False
    elif done_bidding != "no" and done_bidding != "yes":
        print("You don't follow instructions well, do you?")
        exit()

# print("The winner is Someone with a bid of $Something.")