def all_construct(target, words, memo):
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    
    all_possible = []
    for word in words:
        if target.startswith(word):
            new_target = target[len(word):]
            possible = all_construct(new_target, words, memo)
            for item in possible:
                item.append(word)
            if possible:
                all_possible.append(*possible)

    memo[target] = all_possible
    return memo[target]


print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], {})) # [[abc, def]]
print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'], {})) # [[purp, le], [p, ur, p, le]]
