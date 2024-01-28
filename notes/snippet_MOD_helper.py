### In Hacker Rank, quite often that the answer should mod 10**9+7, and many basic functions will break the result.
### Below, record some common functions that might be used when coding Hackerrank.

### How to handle division for big integer?
MOD = 10**9 + 7

def power(x, n, m):
    if n == 1:
        return x % m
    elif n % 2 == 0:
        return power(x ** 2 % m, n // 2, m)
    else:
        return (x * power(x ** 2 % m, (n - 1) // 2, m)) % m
power(2, 2) # 4
power(3, 4) # 81    

    
def devision(a, b):
    return (a * power(b, MOD-2, MOD)) % MOD

devision(100, 10)  ### 100 / 10 = 10
devision(12, 3)  ### 12 / 3 = 4


###### -------------------------------------- ######
###### If face the ERROR: ValueError: Exceeds the limit (4300 digits) for integer string 
###### Or, cannot handle integer that is over 64 bits
import sys
sys.set_int_max_str_digits(500000)   # Set higher if cannot pass