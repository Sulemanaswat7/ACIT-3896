def isPalindrome(s):
    return s == s[::-1]

print(isPalindrome("abba"))        
print(isPalindrome("race car"))    
print(isPalindrome("r aceca r"))   
print(isPalindrome("🙃🙂🙃"))        


def counter(iterable):
    counts = {}
    for item in iterable:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

print(counter("abcabc"))
print(counter(["ab", "ab", "ba", "ba", "aba", "ab"]))
