def how_sum(target, numbers, carry, memo):
    if str(carry) in memo:
        return memo[carry]
    if sum(carry) > target:
        return False
    if sum(carry) == target:
        return True

    for x in numbers:
        carry.append(x)
        memo[str(carry)] = how_sum(target, numbers, carry, memo)
        if memo[str(carry)]:
            return carry

    return []

print(how_sum(8, [2,3,5], [], {}))