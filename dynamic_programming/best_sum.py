def best_sum(target, numbers, memo):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    
    shortest = None
    for x in numbers:
        returned = best_sum(target-x, numbers, memo)
        if returned != None:
            comb = [*returned, x]
            if shortest == None or len(shortest) > len(comb):
               shortest = comb
    memo[target] = shortest
    return shortest



print(best_sum(8, [2,3,5], {}))
print(best_sum(7, [5,3,4,7], {}))
print(best_sum(8, [1,4,5], {}))

