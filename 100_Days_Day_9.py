##################
# Silent Auction #
##################

# Importing the "os" module so that the screen can eventually be cleared for multiple bidders.
import os

# ASCII art for beginning banner/logo (courtesy of https://replit.com/@appbrewery/blind-auction-start#art.py).
banner_logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# Intro to the silent auction.
print(banner_logo)
print("Welcome to the silent auction program.\n")

# Empty dictionary of bidders and bids.
bidders_bids_dictionary = {}

# The "while" loop that is the actual auction process.
continue_bidding = True
while continue_bidding == True:
    # The bidder will be the key.
    bidder = str(input("What is your name?\n"))

    # The bid will be the value.
    bid = int(input("What is your bid?\n"))

    # Putting the key and value together in the dictionary.
    bidders_bids_dictionary[bidder] = bid

    # Offering the chance for other bidders before finishing the auction.
    more_bidders = str(input("Are there any other bidders?  Type \"yes\" or \"no\": ").lower())
    if more_bidders == "yes":
        if os.name == "posix":
            os.system("clear") # Clears the screen for non-Windows OS's.
        else:
            os.system("cls") # Clears the screen for Windows OS's.
    elif more_bidders == "no":
        continue_bidding = False
    else:
        print("You don't follow instructions well, do you?")
        exit()

# Determining the hightest bid.
leading_bid = 0
for bidder_name in bidders_bids_dictionary:
    bid_amount = bidders_bids_dictionary[bidder_name]
    if bid_amount > leading_bid:
        leading_bidder = bidder_name
        leading_bid = bid_amount

# Declaring the winning bidder and bid.
print()
print(f"The winner is {leading_bidder} with a bid of $" + str(leading_bid) + "!  That concludes our silent auction.")