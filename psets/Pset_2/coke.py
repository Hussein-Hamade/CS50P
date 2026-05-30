def amount(coin: int) ->None:
    coke_price = 50
    amount_due = coke_price - coin
    if coin == 50:
        print("Change Owed: ", amount_due)
    else:
        print("Amount Due: ", amount_due)

    while amount_due > 0:
        coin = int(input("Insert Coin: "))
        if check_valid(coin):
            amount_due -= coin
            if amount_due > 0:
                print("Amount Due: ", amount_due)
            else:
                print("Change Owed: ", abs(amount_due))
        else:
            print("invalid coin value")

def check_valid(coin: int) -> bool:
    return coin in [5, 25, 50]


def main():
    while True:
        coin = int(input("Insert Coin: "))
        if check_valid(coin):
            amount(coin)
            break
        else:
            print("invalid coin value")

main()