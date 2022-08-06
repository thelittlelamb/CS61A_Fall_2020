from distutils.command.build_scripts import first_line_re
from unittest import result


def make_bank(balance):
    """
    Returns a bank function with a starting balance. Supports
    withdrawals and deposits.
    """
    def bank(message, amount):
        nonlocal balance
        if message == 'withdraw':
            if amount > balance:
                return 'Insufficient funds'
            balance = balance - amount
            return balance
        elif message == 'deposit':
            balance = balance + amount
            return balance
        else:
            return 'Invalid message'
    return bank


def make_withdraw(balance, password):
    """
    Return a password-protected withdraw function.
    """
    correct_password = password
    wrong_attempt = []
    def withdraw(amount, password_cur):
        nonlocal wrong_attempt, balance
        if len(wrong_attempt) >= 3:
            return 'Frozen account. Attempts: ' + str(wrong_attempt)
        if password_cur == correct_password:
            if amount > balance:
                return 'Insufficient funds'
            else:
                balance = balance - amount
                return balance
        else:
            wrong_attempt.append(password_cur)
            return 'Incorrect password'
    return withdraw


def repeated(t, k):
    """
    Return the first value in iterator T that appears K times in a row. Iterate through the items such that
    if the same iterator is passed into repeated twice, it continues in the second call at the point it left off
    in the first.
    """
    assert k > 1
    # s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    def repeated_helper(k_countdown, pre_v):
        if k_countdown == 1:
            return pre_v
        v = next(t)
        if pre_v == v:
            return repeated_helper(k_countdown - 1, pre_v)
        else:
            return repeated_helper(k, v)
    return repeated_helper(k, next(t))


def permutations(seq):
    """
    Generates all permutations of the given sequence. Each permutation is a
    list of the elements in SEQ in a different order. The permutations may be
    yielded in any order.
    """
    if len(seq) == 1:
        yield seq
    else:
        other_generator, first = permutations(seq[1:]), seq[0]
        for other in other_generator:
            for i in range(len(other) + 1):
                result = list(other[:])
                result[i:i] = [first]
                yield result


def make_joint(withdraw, old_pass, new_pass):
    """
    Return a password-protected withdraw function that has joint access to
    the balance of withdraw.
    """
    vertification = withdraw(0, old_pass)
    if type(vertification) == str:
        return vertification
    def new_withdraw(amount, password):
        if password == new_pass:
            return withdraw(amount, old_pass)
        else:
            return withdraw(amount, password)
    return new_withdraw


def remainders_generator(m):
    """
    Yields m generators. The ith yielded generator yields natural numbers whose
    remainder is i when divided by m.
    generator产生generator, 需要在generator function里面定义一个generator function
    """
    def helper(i):
        for x in naturals():
            if x % m == i:
                yield x
    
    for i in range(m):
        yield helper(i)



def naturals():
    """
    A generator function that yields the infinite sequence of natural
    numbers, starting at 1.
    """
    i = 1
    while True:
        yield i
        i += 1

