### How to handle division for big integer?
MOD = 10**9 + 7

def power(x, n, m):
    if n == 1:
        return x % m
    elif n % 2 == 0:
        return power(x ** 2 % m, n // 2, m)
    else:
        return (x * power(x ** 2 % m, (n - 1) // 2, m)) % m
def devision(a, b):
    return (a * power(b, MOD-2, MOD)) % MOD

devision(100, 10)  ### 100 / 10 = 10
devision(12, 3)  ### 12 / 3 = 4