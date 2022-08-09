def convert_link(link):
    """
    Takes a linked list and returns a Python list with the same elements.
    两种写法：
    1. 利用class link, 模仿__str__ method
    2. recursion
    """
    result = []
    curr_link = link
    while curr_link is not Link.empty:
        result.append(curr_link.first)
        curr_link = curr_link.rest
    return result


def every_other(s):
    """
    Mutates a linked list so that all the odd-indiced elements are removed
    (using 0-based indexing).
    """
    # 原位操作，怎么保证原位操作？
    if s.rest is Link.empty:
        return s
    else:
        if s.rest.rest is Link.empty:
            return Link(s.first)
        else:
            s.rest = every_other(s.rest.rest)


def cumulative_mul(t):
    """
    Mutates t so that each node's label becomes the product of all labels in
    the corresponding subtree rooted at t.
    """
    if t.is_leaf():
        return t
    else:
        for b in t.branches:
            cumulative_mul(b) #原位操作
            t.label *= b.label


def has_cycle(link):
    """
    Return whether link contains a cycle.
    链表末端的next指针指向头结点
    """
    link_have_seen = []
    curr_link = link
    while curr_link.rest is not Link.empty:
        link_have_seen.append(curr_link)
        if curr_link.rest in link_have_seen:
            return True
        curr_link = curr_link.rest
    return False


def has_cycle_constant(link):
    """
    Return whether link contains a cycle.
    """
    # 常数的时间复杂度：快慢指针法
    fast, slow = link, link
    while fast.rest is not Link.empty and fast.rest.rest is not Link.empty and slow.rest is not Link.empty:
        if fast.rest.rest is slow.rest:
            return True
        fast = fast.rest.rest
        slow = slow.rest
    return False


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

