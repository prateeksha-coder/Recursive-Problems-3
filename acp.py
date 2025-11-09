def count_ways(coins, n, amount):
    # If amount is 0, there is 1 solution (do not include any coin)
    if amount == 0:
        return 1

    # If amount is less than 0, no solution exists
    if amount < 0:
        return 0

    # If there are no coins and amount is greater than 0, no solution exists
    if n <= 0 and amount >= 1:
        return 0

    # Count is the sum of solutions including coins[n-1] and excluding coins[n-1]
    return count_ways(coins, n - 1, amount) + count_ways(coins, n, amount - coins[n - 1])


# Example usage
coins = [1, 2, 5]  # coin denominations
amount = 5  # total amount
n = len(coins)

print(f"Number of ways to divide {amount} using coins {coins}: {count_ways(coins, n, amount)}")
