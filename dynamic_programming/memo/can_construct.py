def can_construct(target, words, memo):
    if target in memo:
        return memo[target]
    
    if target == '':
        return True
     
    for word in words:
        if target.startswith(word):
            new_target = target[len(word):]
            memo[new_target] = can_construct(new_target, words, memo)
            if memo[new_target]:
                return True
    
    memo[target] = False
    return False



print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {})) ## false
print(can_construct('santahat', ['san', 'hat', 'a', 't', 'santah'], {})) ## true


# initial complexity, n^m 
# with memoization complexity 