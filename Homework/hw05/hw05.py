from turtle import right


class VendingMachine:
    """
    A vending(销售) machine that vends some product for some price.
    自动售卖机
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.balance = 0
        self.inventory = 0
    
    def add_funds(self, amout):
        if self.inventory:
            self.balance += amout
            return 'Current balance: ${0}'.format(self.balance)
        else:
            return 'Inventory empty. Restocking required. Here is your ${0}.'.format(amout)

    def restock(self, number):
        self.inventory += number
        return 'Current {0} stock: {1}'.format(self.name, self.inventory)

    def vend(self):
        if self.inventory:
            if self.balance >= self.price:
                change = self.balance - self.price
                self.balance = 0
                self.inventory -= 1
                if change:
                    return 'Here is your {0} and ${1} change.'.format(self.name, change)
                else:
                    return 'Here is your {0}.'.format(self.name)
            else:
                return 'You must add ${0} more funds.'.format(self.price - self.balance)
        else:
            return 'Inventory empty. Restocking required.'


class Mint:
    """
    A mint creates coins by stamping on years.
    mint:铸币厂
    The update method sets the mint's stamp to Mint.current_year.
    """
    current_year = 2020

    def __init__(self):
        self.update()

    def create(self, kind):
        return kind(self.year)

    def update(self):
        self.year = Mint.current_year #class attribute


class Coin:
    def __init__(self, year):
        self.year = year

    def worth(self):
        extra_value = max(0, Mint.current_year - self.year - 50)
        # logic: Coin -> Nickel -> Dime self代表instance, self.cents寻找class attribute
        return self.cents + extra_value

class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10


def store_digits(n):
    """
    Stores the digits of a positive number n in a linked list.
    """
    assert isinstance(n, int)
    if n < 10:
        return Link(n)
    else:
        first, rest = split_first_number(n)
        return Link(first, store_digits(rest))

def split_first_number(n):
    """Split a non-negative number N into its first digit and the rest digits."""
    first, rest = n, 0
    digits = 1
    while first >= 10:
        remainder = first % 10
        rest += remainder * digits
        digits *= 10
        first //= 10
    return first, rest

def is_bst(t):
    """
    就是单纯的二叉树，而不是什么完全二叉树
    Returns True if the Tree t has the structure of a valid BST.
    """
    if t.is_leaf():
        return True
    else:
        father, branches = t.label, t.branches
        if len(branches) > 2:
            return False
        elif len(branches) == 1:
            branch = branches[0]
            return is_bst(branch)
        else:
            left_branch, right_branch = branches[0], branches[1]
            # 核心在于：左子树所有的值都<father,右子树所有的值都>father
            if bst_max(left_branch) <= father and father < bst_min(right_branch):
                return is_bst(left_branch) and is_bst(right_branch)
            else:
                return False

def bst_min(t):
    """
    return the minimum value of a bst
    """
    if t.is_leaf():
        return t.label
    elif len(t.branches) == 1: # 如果只有一个子树
        return min(t.branches[0].label, t.label)
    else:
        return bst_min(t.branches[0])

def bst_max(t):
    if t.is_leaf():
        return t.label
    elif len(t.branches) == 1: # 如果只有一个子树
        return max(t.branches[0].label, t.label)
    else:
        return bst_max(t.branches[1])


def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(Tree(2, [Tree(4, [Tree(6)])]))
    [2, 4, 6]
    """
    # [1, 2] + [3] = [1, 2, 3]
    if t.is_leaf():
        return [t.label]
    else:
        preorder_branch = []
        for branch in t.branches:
            preorder_branch.extend(preorder(branch))
        return [t.label] + preorder_branch



def path_yielder(t, value):
    """
    Yields all possible paths from the root of t to a node with the label value
    as a list.
    """
    # yield 和 return 用法是类似的，也可以用于递归
    if t.label == value:
        yield [t.label]

    for branch in t.branches:
        for path in path_yielder(branch, value):
            yield [t.label] + path


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

