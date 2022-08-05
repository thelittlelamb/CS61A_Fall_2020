this_file = __file__


def make_adder_inc(a):
    def adder(t):
        nonlocal a
        a += 1 # 反映了调用次数
        return a + t - 1
    return adder


def make_fib():
    """
    Returns a function that returns the next Fibonacci number
    every time it is called.
    """
    current, next = 0, 0
    def fib():
        nonlocal current, next
        if b == 0:
            b += 1
        else:
            current, next = next, current + next
        return current
    return fib


def insert_items(lst, entry, elem):
    i = 0
    while i < len(lst):
        if lst[i] == entry:
            lst.insert(i + 1, elem)
            # Be careful in situations where the values passed into entry and elem are equivalent
            if entry == elem:
                i += 1
        i += 1
    return lst

