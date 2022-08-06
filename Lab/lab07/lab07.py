def naturals():
    """
    A generator function that yields the infinite sequence of natural
    numbers, starting at 1.
    """
    i = 1
    while True:
        yield i
        i += 1


def scale(it, multiplier):
    """
    Yield elements of the iterable it scaled by a number multiplier.
    """
    for x in it:
        yield x * multiplier


def hailstone(n):
    i = n
    while i != 1:
        yield i
        if i % 2 == 0:
            i //= 2
        else:
            i = i * 3 + 1
    if i == 1:
        yield 1
        

