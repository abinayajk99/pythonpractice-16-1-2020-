==============================================================ASSERTION STATEMENT============================================================
>>>def f():
...    assert 1!=1
...    print('Hello')
>>>f()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in f
AssertionError
>>> try:
...     print('hello')
...     assert 1!=1
... except AssertionError as x:
...     print('error')
... 
hello
error
>>> try:
...     print('Hello')
...     assert 1!=1,"Ganesh"
... except AssertionError as x:
...     print(x)
... 
Hello
Ganesh
>>> try:
...     print('Hello')
...     assert 1==1,"Ganesh"
... except AssertionError as x:
...     print(x)
... 
Hello
>>> def f():
...     assert 1!=1,"ganesh"
... 
>>> f()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in f
AssertionError: ganesh
>>> def f():
...     assert 1!=1,"ganesh"
...     print('hi')
... 
>>> f()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in f
AssertionError: ganesh
>>> 

   =============================================================LAMBDAFUNCTIONS======================================================================
>>> double = lambda x: x * 2
>>> double(10)
20
>>> new_list = list(map(lambda x: x * 2 , [1,2,3,4]))
>>> new_list
[2, 4, 6, 8]
>>> 
=======================================================================DECORATORS=====================================================================

>>>def plus_one(number):
...    return number + 1

>>>add_one = plus_one
>>>add_one(5)
6


>>>def plus_one(number):
...    def add_one(number):
...        return number + 1


...    result = add_one(number)
...    return result
...

>>>plus_one(4)
5


>>>def plus_one(number):
...    return number + 1

>>>def function_call(function):
...    number_to_add = 5
...    return function(number_to_add)
...
>>>function_call(plus_one)
6

>>>def hello_function():
...    def say_hi():
...        return "Hi"
...    return say_hi
>>>hello = hello_function()
>>>hello()
'Hi'

>>>def print_message(message):
...    "Enclosong Function"
...    def message_sender():
...        "Nested Function"
...        print(message)
...    message_sender()

>>>print_message("Some random message")
'Some random message'

>>>def uppercase_decorator(function):
...    def wrapper():
...        func = function()
...        make_uppercase = func.upper()
...        return make_uppercase
...    return wrapper

