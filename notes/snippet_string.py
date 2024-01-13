
# Reverse
s = s[::-1]


# Charactor <----> Number
num = ord(char)
char = chr(num)




# Paradimes  (Like aabbxbbaa)

############## Snippet ################
def is_palindrome(s):
    mid = len(s) // 2
    if len(s) % 2:	
        return s[:mid] == s[mid+1:][::-1]
    else:
        return s[:mid] == s[mid:][::-1]
############## Snippet END ################