def falling(n, k):
    """Compute the falling factorial of n to depth k."""
    if (k == 0):
        return 1
    result = 1
    while (k > 0):
        result *= n
        n -= 1
        k -= 1
    return result


def sum_digits(y):
    """Sum all the digits of y."""
    result = 0
    while (y > 0):
        result += (y % 10)
        y = y // 10
    return result


def double_eights(n):
    """Return true if n has two eights in a row."""
    Number = 0
    while (n > 0):
        mod = n % 10
        if (mod == 8):
            Number += 1
        else:
            Number = 0
        n = n // 10
        if (Number == 2):
            return True
    return False


