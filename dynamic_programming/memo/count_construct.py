def count_construct(target, words, memo):
    if target in memo:
        return memo[target]

    if target == '':
        return 1
    
    count = 0
    for word in words:
        if target.startswith(word):
            new_target = target[len(word):]
            memo[new_target] = count_construct(new_target, words, memo)
            count += memo[new_target]
    memo[target] = count
    return memo[target]


print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], {})) # 1