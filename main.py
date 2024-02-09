def palindrome(word):
    word = word.lower()
    word = word.strip()
    word = word.replace(' ', '')
    if word == '':
        return False
    elif word == word[::-1]:
        return True
    else:
        return False

if __name__ == '__main__': 
    user_word = input()
    print (palindrome(user_word))
    
