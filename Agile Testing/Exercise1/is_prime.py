def is_prime(n):
    i = 2
    while (i <= n ** (1/2)):
        if (n % i == 0):
            return False
        i += 1
    return True