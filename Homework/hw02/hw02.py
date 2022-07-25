HW_SOURCE_FILE=__file__


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.
    """
    if (x == 8):
        return 1
    if (x == 0):
        return 0
    else:
        if (x % 10 == 8):
            return num_eights(x // 10) + 1
        else:
            return num_eights(x // 10)

def mutiple_eight(x):
    if (x % 8 == 0):
        return True
    else:
        return False

def pingpong(n):
    """Return the nth element of the ping-pong sequence.
    """
    # 不能使用赋值语句
    def pingpong_count(k, step, result): # 这个step用的实在是妙极了
        if (k == 1):
            return 1
        elif (k == n):
            return result
        else:
            if (mutiple_eight(n) or num_eights(n) > 0):
                return pingpong_count(k + 1, - step, result - step)
            else:
                return pingpong_count(k + 1, step, result + step)
    return pingpong_count(1, 1, 1)


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    """
    if (n // 10 == 0):
        return 0
    else:
        if ((n % 10) - (n // 10 % 10) >= 1):
            return missing_digits(n // 10) + (n % 10) - (n // 10 % 10) - 1
        else:
            return missing_digits(n // 10)


def next_largest_coin(coin):
    """Return the next coin. 
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(total): #这个树形有点像是树形dp,深度优先搜索
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.                                 
    """
    # 这种题目的思考方式：dp集合划分，有没有最小的or有没有最大的
    # 还有就是边界条件的思考
    def count_coins_helper(money, small_coin):
        if money == 0:
            return 1
        elif money < 0:
            return 0
        elif not small_coin:
            return 0
        else:
            next_coin = next_largest_coin(small_coin)
            return count_coins_helper(money - small_coin, small_coin) + count_coins_helper(money, next_coin)
    return count_coins_helper(total, 1)


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.
    """
    # 把函数当做参数传入，构造call, 在call里用lambda构造这个函数的behavior，这样就解决了迭代时需要函数名的问题。
    return (lambda f: lambda k: f(f, k))(lambda f, k: k if k == 1 else mul(k, f(f, sub(k, 1))))
    # f为函数，返回值是需要k为参数的函数
    # k为需要传入的参数，返回值是f(f, k)
    # 后面一个()是call
    # 感觉还是没懂