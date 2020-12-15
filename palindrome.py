def is_palindrome(word):
    lengh = len(word)
    for i in range(0,lengh):
        if word[i] == word[lengh-1-i]:
            continue
        else:
            return False
    return True
# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
