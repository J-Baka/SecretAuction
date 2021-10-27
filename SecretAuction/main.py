from replit import clear

from art import logo

print(logo)

bids = {}
final_bid = False


def highest_bidder(bid_records):
    highest_bet = 0
    for bid in bid_records:
        bid_value = bid_records[bid]
        if bid_value > highest_bet:
            highest_bet = bid_value
            winner = bid

    print(f"The winner of the auction is {winner} with a bid of ${highest_bet}")


# Will loop user responses until there are no more bets being placed

while not final_bid:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))

    bids[name] = price
    user_answer = input("Are there any other bidders? Please type 'Yes' or 'No': ")

    if user_answer == "No":
        final_bid = True
        highest_bidder(bids)
    elif user_answer == "Yes":
        clear()
