def can_sum(n, ints, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        return True
    if n < 0:
        return False

    for x in ints:
        memo[n-x] = can_sum(n-x, ints, memo)
        if memo[n-x] == True:
            return True
    return False 



print(can_sum(7, [5,3,4,7], {}))
print(can_sum(2, [5,3,4,7], {}))
print(can_sum(300, [7,14], {}))