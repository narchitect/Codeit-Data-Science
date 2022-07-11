def is_palindrome(word):
    central_word_num = int(len(word)//2)
    
    for i in range(central_word_num):
        front_word = word[i]
        back_word = word [-(i+1)]
        if front_word != back_word:
            return False
        elif i == central_word_num-1:
            return True
    
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))