coinvaluelist = [1, 5, 10, 25]
known = {}


def minC(target):
    mincoins = target

    if target in coinvaluelist:
        return 1
    elif target in known:
        return known[target]
    else:
        for coin in coinvaluelist:
            if coin <= target:
                numcoins = 1 + minC(target - coin)
                known[target] = numcoins
                mincoins = min(numcoins, mincoins)

    return mincoins


print(minC(63))
