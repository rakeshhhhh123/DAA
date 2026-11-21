print("Making Change Problem")

coins = list(map(int, input("Enter the coin values: ").split()))
amount = int(input("Enter the amount: "))

dp = [amount + 1] * (amount + 1)
dp[0] = 0

for current in range(1, amount + 1):
    for coin in coins:
        if coin <= current:
            dp[current] = min(dp[current], dp[current - coin] + 1)

if dp[amount] == amount + 1:
    print("Change cannot be made")
else:
    print("Minimum number of coins:", dp[amount])

    remaining = amount
    used_coins = []

    while remaining > 0:
        for coin in coins:
            if coin <= remaining and dp[remaining] == dp[remaining - coin] + 1:
                used_coins.append(coin)
                remaining = remaining - coin
                break

    print("Coins used:", used_coins)
