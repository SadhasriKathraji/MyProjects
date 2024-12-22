import os
print("welcome to the Silent Auction Program")
bidder_data = {}

def find_winner(bidder_details):            #{'sadaa':20000,'sam':15000,'sue':19000}
    highest_bid = 0
    winner = ""
    for key in bidder_details:              #sadaa
        bid_price = bidder_details[key]     #20000
        if bid_price > highest_bid:
            highest_bid = bid_price
            winner = key
    print(bidder_details)
    print(f"The winner is {winner} with a bid price of {highest_bid}")
end_of_bidding = False
while not end_of_bidding:
    name = input("what's your name?:")
    price = int(input("what's your bid?:"))
    bidder_data[name] = price
    #print(bidder_data)
    more_bidders = input("Are there more bidders? yes or no:")
    if more_bidders == "no":
        end_of_bidding = True
        find_winner(bidder_data)
    elif more_bidders == "yes":
        os.system('cls')