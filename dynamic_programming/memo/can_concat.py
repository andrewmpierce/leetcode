# Write a function, canConcat, that takes in a string and an array of words 
# as arguments. The function should return boolean indicating whether or 
# not it is possible to concatenate words of the array together to form the string.



def can_concat(string, words, memo):
    if string in memo:
        return memo[string]
    if string == "":
        return True
    
    for word in words:
        if string.startswith(word):
            new = string[len(word):]
            if can_concat(new, words, memo):
                memo[string] = True
                return True
    memo[string] = False
    return False



print(can_concat("oneisnone", ["one", "none", "is"], {})) ## true
print(can_concat("oneisnone", ["on", "e", "is"], {})) ## false
print(can_concat("oneisnone", ["on", "e", "is", "n"], {})) ## true
print(can_concat("santahat", ["santah", "hat"], {})) ## false
print(can_concat("santahat", ["santah", "san", "hat", "tahat"], {})) ## true
