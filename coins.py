

def exchange(coins, change):
    """
    >>> exchange([1, 5, 10], 26)
    4
    """
    global num_calls
    num_calls += 1
    min_coins = change
    if change in coins:
        return 1
    else:
        for i in [c for c in coins if c <= change]:
            num_coins = 1 + exchange(coins, change - i)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins


num_calls = 0
exchange([1, 5, 10, 25], 63)
print(num_calls)
