# CS61A

# ==2 Data==

## 2.1 Introduction

## 2.2 Data Abstraction

<font color='red'>When writing functions that use an ADT, we should use the constructor(s) and selector(s) whenever possible instead of assuming the ADT's implementation. Relying on a data abstraction's underlying implementation is known as *violating the abstraction barrier*, and we never want to do this!</font>

简而言之，抽象出来的数据类型有可能是列表，也有可能字典，所以我们需要手动constructors

## 2.3 Sequences

> * length
> * element selection

### 1 Lists

```python
digits = [1, 8, 2, 8]
len(digits)
digits[3] #element selection
```

### 2 Sequence Iteration

* A `for` statement consists of a single clause with the form:

  >1. Evaluate the header `<expression>`, which must yield an iterable value.
  >2. For each element value in that iterable value, in order:
  >   1. Bind `<name>` to that value in the current frame.
  >   2. Execute the `<suite>`.

  ```python
  for <name> in <expression>:
      <suite>
  ```

* **Ranges.** A `range` is another built-in type of sequence in Python, which represents a range of integers. Ranges are created with `range`, which takes two integer arguments: the first number and one beyond the last number in the desired range.

  ```python
  >>> range(1, 10)  # Includes 1, but not 10
  range(1, 10)
  
  >>> list(range(4))
  [0, 1, 2, 3]
  ```

### 3 Sequence Processing

* **List Comprehensions.** Many sequence processing operations can be expressed by **evaluating a fixed expression for each element in a sequence** and collecting the resulting values in a result sequence. 

  ```python
  [<map expression> for <name> in <sequence expression> if <filter expression>]
  ```

  ```python
  >>> odds = [1, 3, 5, 7, 9]
  >>> [x+1 for x in odds]
  
  # satisfy some condition
  >>> [x for x in odds if 25 % x == 0]
  ```

* **Aggregation.**  `sum`, `min`, and `max`

* **Higher-Order Functions.** 

  ```python
  def apply_to_all(map_fn, s):
      return [map_fn(x) for x in s]
  ```
  
* **Conventional Names.**

  ```python
  apply_to_all = lambda map_fn, s: list(map(map_fn, s))
  keep_if = lambda filter_fn, s: list(filter(filter_fn, s))
  ```


###  4 Sequence Abstraction

* **Membership**.  A value can be tested for membership in a sequence.

  > two operators `in` and `not in` 

* **Slicing.** Sequences contain smaller sequences within them.

### 5 Strings

* String literals can express arbitrary text, surrounded by either single or double quotation marks

  ```python
  "I've got an apostrophe"
  '您好'
  ```

* They have a length and they support element selection.

* Like lists, strings can also be combined via **addition and multiplication.**

  ```python
  >>> 'Berkeley' + ', CA'
  'Berkeley, CA'
  >>> 'Shabu ' * 2
  'Shabu Shabu 
  ```

* **Membership**

* **Multiline Literals.** 

* **String Coercion.** A string can be created from any object in Python by calling the `str` constructor function with an object value as its argument. 

  ```python
  >>> str(2) + ' is an element of ' + str(digits)
  '2 is an element of [1, 8, 2, 8]'
  ```

### 6 Trees

>a *closure property*：use lists as the elements of other lists

* A tree has a root label and a sequence of branches. 

  > The *tree* is a fundamental data abstraction that imposes regularity on how hierarchical values are structured and manipulated.

* The data abstraction for a tree consists of the constructor `tree` and the selectors `label` and `branches`.

  * tree construction：

  ```python
  def tree(root_label, branches=[]):
      for branch in branches:
          assert is_tree(branch), 'branches must be trees'
          return [root_label] + list(branches)
  def label(tree):
      return tree[0]
  def branches(tree):
      return tree[1:]
  
  # example
  t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
  >>> t
  [3, [1], [2, [1], [1]]]
  ```

  * property

  ```python
  def is_tree(tree):
      if type(tree) != list or len(tree) < 1:
      	return False
      for branch in branches(tree):
      	if not is_tree(branch):
      		return False
      return True
  
  def is_leaf(tree):
      return not branches(tree)
  ```

* **A binary tree.**  Slicing can be used on the branches of a tree as well. 

  ```python
  def right_binarize(tree):
      """Construct a right-branching binary tree."""
      if is_leaf(tree):
      	return tree
      if len(tree) > 2:
      	tree = [tree[0], tree[1:]]
      return [right_binarize(b) for b in tree]
  
  # example
  >>> right_binarize([1, 2, 3, 4, 5, 6, 7])
  [1, [2, [3, [4, [5, [6, 7]]]]]]
  ```


### 7 Linked Lists

```python
#example
four = [1, [2, [3, [4, 'empty']]]]
```

* A linked list is a pair containing **the first element of the sequence**  and **the rest of the sequence**. The second element is also a linked list. 

  > the rest of a linked list is a linked list or `'empty'`. 

  ```python
  empty = 'empty'
  def is_link(s):
      """s is a linked list if it is empty or a (first, rest) pair."""
      return s == empty or (len(s) == 2 and is_link(s[1]))
  def link(first, rest):
      """Construct a linked list from its first element and the rest."""
      assert is_link(rest), "rest must be a linked list."
      return [first, rest]
  def first(s):
      """Return the first element of a linked list s."""
      assert is_link(s), "first only applies to linked lists."
      assert s != empty, "empty linked list has no first element."
      return s[0]
  def rest(s):
      """Return the rest of the elements of a linked list s."""
      assert is_link(s), "rest only applies to linked lists."
      assert s != empty, "empty linked list has no rest."
      return s[1]
  ```

  ```PYTHON
  def len_link(s):
      """Return the length of linked list s."""
      length = 0
      while s != empty:
          s, length = rest(s), length + 1
          return length
  def getitem_link(s, i):
      """Return the element at index i of linked list s."""
      while i > 0:
          s, i = rest(s), i - 1
          return first(s)
  ```

  * each step in an iteration operates on an increasingly shorter suffix of the original list. 

* **Recursive manipulation.** Both `len_link` and `getitem_link` are iterative.

  >so, it needs time

* **Recursive manipulation.** The recursive implementations follow the chain of pairs until the end of the list (in `len_link_recursive`) or the desired element (in `getitem_link_recursive`) is reached.

  ```python
  def extend_link(s, t):
      """Return a list with the elements of s followed by those of t."""
      assert is_link(s) and is_link(t)
      if s == empty:
          return t
      else:
          return link(first(s), extend_link(rest(s), t))
  
  def apply_to_all_link(f, s):
      """Apply f to each element of s."""
      assert is_link(s)
      if s == empty:
          return s
      else:
          return link(f(first(s)), apply_to_all_link(f, rest(s)))
  
  def keep_if_link(f, s):
      """Return a list with elements of s for which f(e) is true."""
      assert is_link(s)
      if s == empty:
          return s
      else:
          kept = keep_if_link(f, rest(s))
          if f(first(s)):
              return link(first(s), kept)
          else:
              return kept
  
  def join_link(s, separator):
      """Return a string of all elements in s separated by separator."""
      if s == empty:
          return ""
      elif rest(s) == empty:
          return str(first(s))
      else:
          return str(first(s)) + separator + join_link(rest(s), separator)
  ```

## 2.4 Mutable Data

### 1  The Object Metaphor

* *Objects* combine data values with behavior.

* Objects have *attributes*, which are named values that are part of the object. We use dot notation to designated an attribute of an object.

  `<expression> . <name>`

* Objects also have *methods*, which are function-valued attributes. By implementation, methods are functions that compute their results from both their arguments and their object. 

### 2  Sequence Objects

* Lists on the other hand are *mutable*.

  >an object may have changing properties due to *mutating* operations.

  ```python
  >>> chinese = ['coin', 'string', 'myriad']  # A list literal
  >>> suits = chinese                         # Two names refer to the same list
  
  >>> suits.pop()             # Remove and return the final element
  'myriad'
  >>> suits.remove('string')  # Remove the first element that equals the argument
  
  >>> suits.append('cup')              # Add an element to the end
  >>> suits.extend(['sword', 'club'])  # Add all elements of a sequence to the end
  
  suits[2] = 'spade'  # Replace an element
  suits[0:2] = ['heart', 'diamond']  # Replace a slice
  # s[i:i] = [x] behaves like insert
  ```

  * Methods also exist for inserting, sorting, and reversing lists.

    > All of these mutation operations change the value of the list; they do not create new list objects.

* **Sharing and Identity.** This behavior is new.

  >With mutable data, methods called on one name can affect another name at the same time.(<font color='red'>引用？</font>)

  * Lists can be copied using the `list` constructor function. 

    ```python
    >>> nest = list(suits)  # Bind "nest" to a second list with the same elements
    >>> nest[0] = suits     # Create a nested list
    ```

  * we require a means to test whether two objects are the same.  `is` and `is not`

    >Identity is a stronger condition than equality.

    ```python
    >>> suits is ['heart', 'diamond', 'spade', 'club']
    False
    >>> suits == ['heart', 'diamond', 'spade', 'club']
    True
    ```

* **Tuples.** A tuple, an instance of the built-in `tuple` type, is an immutable sequence.

  ```python
  >>> code = ("up", "up", "down", "down") + ("left", "right") * 2
  >>> len(code)
  8
  >>> code[3]
  'down'
  >>> code.count("down")
  2
  >>> code.index("left")
  4
  ```

### 3  Dictionaries

* A dictionary contains key-value pairs, where both the keys and values are objects.

* Dictionaries are unordered collections of key-value pairs. When we print a dictionary, <font color='red'>the keys and values are rendered in some order(unknown)</font>, but as users of the language we cannot predict what that order will be. 

* The methods `keys`, `values`, and `items` all return iterable values.

  ```python
  sum(numerals.values())
  ```

* calling the `dict` constructor function.

  ```python
  dict([(3, 9), (4, 16), (5, 25)])
  ```

* A useful method implemented by dictionaries is `get`, which returns either the value for a key, if the key is present, or a default value. <font color='red'>The arguments to `get` are the key and the default value.</font>

  ```python
  >>> numerals.get('A', 0)
  0
  >>> numerals.get('V', 0)
  5
  ```

* **comprehension syntax**

  ```python
  {x: x*x for x in range(3,6)}
  ```

### 4  Local State

* Lists and dictionaries have *<font color='red'>local state</font>*: they are changing values that have some particular contents at any point in the execution of a program. 

  ```python
  def make_withdraw(balance):
      """Return a withdraw function that draws down balance with each call."""
      def withdraw(amount):
          nonlocal balance                 # Declare the name "balance" nonlocal
          if amount > balance:
              return 'Insufficient funds'
          balance = balance - amount       # Re-bind the existing balance name
          return balance
      return withdraw
  ```

* **Python Particulars.** Python also has an unusual restriction regarding the lookup of names: within the body of a function, all instances of a name must refer to the same frame. 

* The key to correctly analyzing code with non-local assignment is to remember that <font color='red'>**only function calls can introduce new frames**</font>. Assignment statements always change bindings in existing frames. 



## 2.5  Object-Oriented Programming

### 1  Objects and Classes

* A class serves as a template for all objects whose type is that class. Every object is an instance of some particular class.

  >instance has its own local state

### 2  Defining Classes

```python
class <name>:
    <suite>
```

```python
class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance
```

* The `__init__` method for `Account` has two formal parameters. The first one, `self`, is bound to the newly created `Account` object. The second parameter, `account_holder`, is bound to the argument passed to the class when it is called to be instantiated.

* The function value that is created by a `def` statement within a `class` statement is **bound to the declared name**, but **bound locally within the class as an attribute**. <font color='red'>That value is invoked as a method using dot notation from an instance of the class</font>.

  >the `self` parameter is bound automatically.

### 3  Message Passing and Dot Expressions

* Objects also have **named local state values** (the instance attributes), but that state can be accessed and manipulated using dot notation, without having to employ `nonlocal` statements in the implementation.

* As we have seen, a dot expression consists of an expression, a dot, and a name:

  ```python
  <expression> . <name>
  ```

  To evaluate a dot expression:

  1. Evaluate the `<expression>` to the left of the dot, which yields the *object* of the dot expression.
  2. `<name>` is matched against the instance attributes of that object; if an attribute with that name exists, its value is returned.
  3. If `<name>` does not appear among instance attributes, then `<name>` is looked up in the class, which yields a class attribute value.
  4. That value is returned unless it is a function, in which case a bound method is returned instead.

  >In this evaluation procedure, instance attributes are found before class attributes, just as local names have priority over global in an environment.

### 4  Class Attributes

* Some attribute values are shared across all objects of a given class. 
* a single assignment statement to a class attribute changes the value of the attribute for all instances of the class.

### 5  Inheritance

*  In OOP terminology, the generic account will serve as the base class of `CheckingAccount`, while `CheckingAccount` will be a subclass of `Account`. (The terms *parent class* and *superclass* are also used for the base class, while *child class* is also used for the subclass.)
* 小结：
  1. 情况一：**子类需要自动调用父类的方法：**子类不重写__init__()方法，实例化子类后，会自动调用父类的__init__()的方法。
  2. 情况二：**子类不需要自动调用父类的方法：**子类重写__init__()方法，实例化子类后，将不会自动调用父类的__init__()的方法。
  3. 情况三：**子类重写__init__()方法又需要调用父类的方法：**使用super关键词
* Inheritance is meant to represent *is-a* relationships between classes

* In fact, the act of "looking up" a name in a class tries to<font color='red'> find that name in every base class in the inheritance chain for the original object's class</font>.

## 2.8  Efficiency

## 2.9  Recursive Objects

* Objects can have other objects as attribute values. When an object of some class has an attribute value of that same class, it is a recursive object.

### 1  Linked List Class

```python
class Link:
    """
    A linked list.
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
        
    def __getitem__(self, i):
            if i == 0:
                return self.first
            else:
                return self.rest[i-1]
            
    def __len__(self):
        return 1 + len(self.rest)

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
```

* `__len__`：The built-in Python function `len` invokes a method called `__len__` when applied to a user-defined object argument. 

  > 如果一个类表现得像一个`list`，要获取有多少个元素，就得用`len()`函数。
  > 要让`len()`函数工作正常，类必须提供一个特殊方法`__len__()`，它返回元素的个数。

* Rather than list comprehensions, one linked list can be generated from another using two higher-order functions: `map_link` and `filter_link`. 

  ```python
  def map_link(f, s):
      if s is Link.empty:
          return s
      else:
          return Link(f(s.first), map_link(f, s.rest))
  ```

  ```python
  def filter_link(f, s):
      if s is Link.empty:
          return s
      else:
          filtered = filter_link(f, s.rest)
          if f(s.first):
              return Link(s.first, filtered)
          else:
              return filtered
  ```

### 2  Tree Class

>前面讲过

### 3  Sets



# ==3 Interpreting Computer Programs==



## 2  Functional Programming

> Scheme is a Dialect of Lisp
>
> 函数式编程最重要的概念就是：组合
>
> 一个函数只做一件事， 保证内部不被修改，且干净，无副作用，遵循开闭原则，然后将多个函数组合一起，便是简单的函数式编程范式

### 1  Expressions

* **Primitive expressions**: `2` `3.3` `true` `+` `quotient`

* **Combinations**: `(quotient 10 2)`` (not true)`

  >Call expressions include an operator and 0 or more operands in parentheses

```scheme
(+ (* 3
      (+ (* 2 4)
         (+ 3 5)))
   (+ (- 10 7)
      6))
```

* **if expression**:

  ```scheme
  (if <predicate> <consequent> <alternative>)
  ```

* **and** and **or**:

  ```scheme
  (and <e1> ... <en>) ;short cut
  (or <e1> ... <en>)
  ```

* **Binding symbols**

  ```scheme
  (define <symbol> <expression>)
  
  (define pi 3.14)
  (* pi 2) ;The symbol “pi” is bound to 3.14 in the global frame
  ```

* **New procedures**

  ```scheme
  (define (<name> <formal parameters>) <body>)
  
  (define (square x) (* x x)) ;return是square
  ```

* **Lambda Expressions**

  ```scheme
  lambda (<formal-parameters>) <body>
  ```

  * Lambda expressions evaluate to anonymous procedures

  * An operator can be a call expression too:

    ```scheme
    ((lambda (x y z) (+ x y (square z))) 1 2 3)
    ```

### 2  Special Forms(Expressions)

* **Cond**:behaves like if-elif-else statements in Python

  ```scheme
  (cond((> x 10) (print 'big))
       ((> x 5) (print 'medium))
       (else (print 'small)))
  ```

* The **begin** special form combines multiple expressions into one expression

  ```scheme
  (cond ((> x 10) (begin (print 'big) (print 'guy)))
  	  (else     (begin (print 'small) (print 'fry))))
  ```

* **Let** Expressions:binds symbols to values temporarily; just for one expression

* **While Statements**

  ```scheme
   (define (f x total)
    (if (< x 10)
        (f (+ x 2) (+ total (* x x)))
        total)
    )
  (f 2 0)
  ```

### 3  Lists

* Rules:
  * `cons`: Two-argument procedure that creates a linked list 
  * `car`: Procedure that returns the first element of a list 
  * `cdr`: Procedure that returns the rest of a list 
  * `nil`: The empty list

* Important! Scheme lists are written in parentheses with elements separated by spaces

  ```scheme
  > (cons 2 nil)
  (1 2)
  > (cons 1 (cons 2 (cons 3 (cons 4 nil))))
  (1 2 3 4)
  ```

### 4  Symbolic Data

* Symbols normally refer to values; how do we refer to symbols?

  ```scheme
  > (define a 1)
  > (define b 2)
  > (list a b)
  (1 2)
  ```

* Quotation is used to refer to symbols directly in Lisp

  ```scheme
  > (list 'a 'b)
  (a b)
  > (list 'a b) ;the expression itself is the value.
  (a 2)
  ```

* Quotation can also be applied to combinations to form lists.

  ```scheme
  > '(a b c)
  (a b c)
  ```

### 5 Programs as Data

* A Scheme Expression is a Scheme List

  * The built-in Scheme list data structure (which is a linked list) can represent combinations

    ```scheme
    scm> (list 'quotient 10 2)
    (quotient 10 2)
    scm> (eval (list 'quotient 10 2))
    5
    ```



```

```



# ==4 Data Processing==

## 4.2  Implicit Sequences

* why we need `iterators`

  >A sequence can be represented without each element being stored explicitly in the memory of the computer.  Instead, we compute elements <font color='red'>on demand.</font>

### 1  Iterators

* **An *iterator*** is an object that provides sequential access to values, one by one.

  * `iter(iterable)`: Return an iterator over the elements of an iterable value 
  * `next(iterator)`: Return the next element in an iterator

  ```python
  >>> s = [3, 4, 5]
  >>> t = iter(s)
  >>> next(t)
  3
  >>> next(t)
  4
  >>> u = iter(s)
  >>> next(u)
  3
  >>> next(t)
  5
  >>> next(u)
  4
  ```

* While not as flexible as accessing arbitrary elements of a sequence (called *random access*), *sequential access* to sequential data is often sufficient for data processing applications.

### 2  Iterables

* Any value that can produce iterators is called an *iterable* value. 

* Iterables include sequence values such as strings and tuples, as well as other containers such as sets and dictionaries. <font color='red'>Iterators are also iterables</font>, because they can be passed to the `iter` function.

* <font color='red'>all iterators are mutable</font>

  >A dictionary, its keys, its values, and its items are all iterable values 
  >
  >The order of items in a dictionary is the order in which they were added 

### 3  Built-in Iterators

* Several built-in functions take as arguments iterable values and return iterators. These functions are used extensively for lazy sequence processing.

  ```python
  >>> def double_and_print(x):
          print('***', x, '=>', 2*x, '***')
          return 2*x
  >>> s = range(3, 7)
  >>> doubled = map(double_and_print, s)  # double_and_print not yet called
  >>> next(doubled)                       # double_and_print called once
  *** 3 => 6 ***
  6
  >>> next(doubled)                       # double_and_print called again
  *** 4 => 8 ***
  ```

  * map(func, iterable)
  * filter(func, iterable)
  * zip(first_iter, second_iter)
  * reversed(sequence)

* To view the contents of an iterator, place the resulting elements into a container 

  ```python
  list(iterable) # Create a list containing all x in iterable
  tuple(iterable)
  sorted(iterable)
  ```

### 4  For Statements

* The `for` statement in Python operates on iterators. Objects are *iterable* (an interface) if they have an `__iter__` method that returns an *iterator*.

  ```python
  >>> counts = [1, 2, 3]
  >>> for item in counts:
          print(item)
  ```

* In the above example, the `counts` list returns an iterator from its `__iter__()` method. The `for` statement then calls that iterator's `__next__()` method repeatedly, and assigns the returned value to `item` each time. 

### 5  Generators and Yield Statements

* <font color='red'>A generator function is a function that yields values instead of returning them</font>

* A generator is an iterator created automatically by calling a generator function

  >When a generator function is called, it returns a generator that iterates over its yields

```python
def letters_generator():
    current = 'a'
    while current <= 'd':
        yield current
        current = chr(ord(current)+1)
```

* <font color='red'>yield和return</font>
  * 相同点： 都是定义函数过程中返回值
  * 不同点：
    1. yield是暂停函数，return是结束函数； 即<font color='red'>**yield返回值后继续执行函数体内代码**</font>，return返回值后不再执行函数体内代码
    2. yield返回的是一个迭代器（yield本身是生成器-生成器是用来生成迭代器的）



# Optional

* `dict`: If I have a Python dictionary, how do I get the key to the entry which contains the minimum value?

  ```python
  >>> min(d, key=d.get)
  321
  # min() return the value in the first value in sorted. key designate the way to sort the values. key=d.get means the list will be sorted by values of the dictionary.
  ```

## 1 Binary Numbers

* How do we encode negative numbers?

  1. start with an unsigned 4-bit binary number where leftmost bit is 0 

     `• 0110 = 6`

  2. complement your binary number (flip bits) 

     `• 1001 `

  3. add one to your binary number

     `• 1010 = -6`

* How do we encode fractional numbers?
  $$
  ± mantissa \times base ^{± exponent}
  $$

* Boolean Logic
