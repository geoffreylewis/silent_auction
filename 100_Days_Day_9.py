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
    print(bidder) # TEST CODE

    # The bid will be the value.
    bid = int(input("What is your bid?\n"))
    print(bid) # TEST CODE

    # Putting the key and value together in the dictionary.
    bidders_bids_dictionary[bidder] = bid
    print(bidders_bids_dictionary) # TEST CODE

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

# print("The winner is Someone with a bid of $Something.")