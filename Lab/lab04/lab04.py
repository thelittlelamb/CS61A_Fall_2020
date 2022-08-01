LAB_SOURCE_FILE = __file__

this_file = __file__

# 作业主题：Recursion, Tree Recursion, Python Lists
def skip_add(n):
    """ 
    Takes a number n and returns n + n-2 + n-4 + n-6 + ... + 0.
    """
    # 不能循环，递归实现
    return 0 if (n <= 0) else (n + skip_add(n - 2))

def summation(n, term):

    """
    Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!
    """
    assert n >= 1
    return term(1) if (n == 1) else term(n) + summation(n - 1, term)


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.
    分析：只能从左边过来or右边过来
    实际上就是优化一下就是dp问题
    """
    return 1 if (m == 1 or n == 1) else paths(m - 1, n) + paths(m, n - 1)


def max_subseq(n, t):
    """
    Return the maximum subsequence of length at most t that can be found in the given number n.
    最大子序列问题
    """
   
    res = 0
    if (n // 10 == 0 or t == 0):
         # 递归停止的条件
        return res
    else:
        # 考虑末位，如果使用末位，如果不使用末位
        return max(res * 10 + max_subseq(n // 10, t - 1), res + max_subseq(n // 10, t - 1))


def add_chars(w1, w2):
    """
    Return a string containing the characters you need to add to w1 to get w2.
    You may assume that w1 is a subsequence of w2.
    """
    res = ''
    if (len(w1) == len(w2)):
        return res
    elif (len(w1) == 0):
        return (res + w2)
    else:
        # 看看是否使用第一个字母
        if(w1[0] == w2[0]):
            return res + add_chars(w1[1:], w2[1:])
        else:
            #第一个不相等，w1指针后移
            return res + w2[0] + add_chars(w1, w2[1:])
