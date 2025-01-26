#initializing constant variables
PRICE_OF_COKE = 50
ACCEPTED_COINS = [5, 10, 25]

def main():
    """
    track the amount inserted and set amount due = PRICE_OF_COKE
    ask for the user's input
    call a coin validity function to check the user's input
    update to amount inserted if it evaluates to true
    """

    amount_inserted = 0
    amount_due = PRICE_OF_COKE
    while True:
        print(f"Amount Due: {amount_due}")

        coin_inserted = int(input("Insert Coin: "))
        if coin_validity(coin_inserted):
            amount_inserted += coin_inserted

            amount_due, change_owed = calc_amount_due(amount_inserted)
            if amount_due == 0:
                print(f"Change Owed: {change_owed}")
                break

def coin_validity(coin_inserted):
    return coin_inserted in ACCEPTED_COINS

def calc_amount_due(amount_inserted):
    """track the amount due and change owed"
    subtract amount due if its less than price of coke and update amount due
    update amount due if price of coke is equal to amount inserted
    update amount due if price of coke is equal to amount inserted is > price of coke
    """
    amount_due = 0
    change_owed = 0
    if amount_inserted < PRICE_OF_COKE:
        amount_due = PRICE_OF_COKE - amount_inserted
    elif amount_inserted == PRICE_OF_COKE:
        amount_due = 0
    elif amount_inserted > PRICE_OF_COKE:
        change_owed = amount_inserted - PRICE_OF_COKE
    
    return amount_due, change_owed


main()