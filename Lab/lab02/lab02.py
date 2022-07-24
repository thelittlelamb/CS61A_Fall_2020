def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    For example, we can write a function f(x, y) as a different function g(x)(y). This is known as currying.
    作用是使得每次传入一个参数？虽然不知道这个有什么用
    """
    return lambda x: lambda y: func(x, y)



def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    """
    def function(N):
        count, i = 0, 1
        while(i <= N):
            if condition(N, i): #condition需要传入两个参数
                count += 1
            i += 1
        return count
    return function

def compose1(f, g):
    """Return the composition function which given x, computes f(g(x)).
    """
    return lambda x: f(g(x))

def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    """
    def compare(x):
        # a = lambda x: f(g(x)) 返回的是一个函数
        a = compose1(f, g)(x)
        b = compose1(g, f)(x)
        flag = False
        if (a == b):
            flag = True
        return flag
    return compare



def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.
    """
    def my_cycle(n):
        def compute(x):
            cycle_time, result = n, x
            count = 1
            while (count <= cycle_time):
                if (count % 3 == 1):
                    result = f1(result)
                elif (count % 3 == 2):
                    result = f2(result)
                else:
                    result = f3(result)
                count += 1
            return result
        return compute
    return my_cycle

