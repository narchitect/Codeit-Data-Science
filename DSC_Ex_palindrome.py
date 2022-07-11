def is_palindrome(word):
    
    words_len = len(word)
    central_num= int((words_len-1)/2)
    front_words = word[:central_num]
    reversed_words = word[::-1]
    back_words = reversed_words[:central_num]
 
    
    if (words_len%2) == 0:
        return False
    elif front_words == back_words:
        return True
    else:
        return False
    

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))