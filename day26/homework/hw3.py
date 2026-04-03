def palindromi(word):
    if word == word[::-1]:
        return True
    else:
        return False
    print(palindromi("level")) 
print(palindromi("hello"))  