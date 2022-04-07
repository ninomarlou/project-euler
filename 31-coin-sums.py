import itertools
import functools


def main():
    x = coin_sums(200)
    print(x)


def coin_sums(target):

    coin_combinations = [[[0]], [[200]]]
    coins = [100, 50, 20, 10, 5, 2, 1]
    for coin in coins:
        coin_combinations = create_combination(coin_combinations, coin, target)

    return len(coin_combinations)


def create_combination(coin_combinations, coin, target):
    result = []
    for coin_combination in coin_combinations:
        for curr_coin in range(0, target + 1, coin):
            if coin != 1:
                if sum(coin_combination[0] + [curr_coin]) <= target:
                    result.append([coin_combination[0] + [curr_coin]])
            else:
                if sum(coin_combination[0] + [curr_coin]) == target:
                    result.append([coin_combination[0] + [curr_coin]])

    return result


if __name__ == "__main__":
    main()
