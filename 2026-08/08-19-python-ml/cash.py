c = int(input("Change owed: "))
coins = 0
for denom in [25, 10, 5, 1]:
    coins += c // denom
    c %= denom
print(coins)
