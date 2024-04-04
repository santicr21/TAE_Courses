def is_prime(n):
    i = 2
    ans = True if n > 1 else False
    if n != 0:
        while (i <= n ** (1/2)):
            if (n % i == 0):
                ans = False
            i += 1
    return ans