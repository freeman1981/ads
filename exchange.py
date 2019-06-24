def exchange1(coins, change):
    """
    >>> exchange1([1, 2, 5, 10], 11)
    2
    >>> exchange1([1, 2, 5, 10], 33)
    5
    """
    min_coins = change
    if change in coins:
        return 1
    else:
        for i in [c for c in coins if c <= change]:
            num_coins = 1 + exchange1(coins, change - i)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins


def exchange2(coins, change, mem):
    """
    >>> exchange2([1, 2, 5, 10], 33, {})
    5
    """
    min_coins = change
    if change in mem:
        return mem[change]
    elif change in coins:
        mem[change] = 1
        return 1
    else:
        for i in [c for c in coins if c <= change]:
            num_coins = 1 + exchange1(coins, change - i)
            if num_coins < min_coins:
                min_coins = num_coins
    mem[change] = min_coins
    return min_coins


def dp_make_change(coin_value_list, change, min_coins):
    """
    >>> dp_make_change([1, 2, 5, 10], 33, {})
    5
    """
    for cents in range(change + 1):
        coin_count = cents
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
        min_coins[cents] = coin_count
    return min_coins[change]
