# Uses python3
import sys

def optimal_coin(coins, amt):

    if amt == 0:
        return []
    for coin in coins:
        if coin <= amt:
            return [coin] + optimal_coin(coins, amt-coin)

def get_change(m):

    coins = [1, 5, 10]
    coins = sorted(coins, reverse=True)

    return len(optimal_coin(coins, m))


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
