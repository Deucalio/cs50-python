cents = 0
while cents != 50:
    print(f"Amount Due: {50-cents}")
    coin = int(input("Insert Coin: "))
    if (coin == 25 or coin == 10 or coin == 5):
        cents += coin
        if (cents >= 50):
            print(f"Change Owed: {cents-50}")
            break
    continue
