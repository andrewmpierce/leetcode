def isPalindrome(num):
    num = [int(x) for x in str(num)]
    if len(num) == 1:
        return True
    left = 0
    right = len(num) -1
    while left < right:
        if num[left] == num[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

assert isPalindrome(121) == True
assert isPalindrome(554) == False
assert isPalindrome(5445) == True
assert isPalindrome(5545) == False