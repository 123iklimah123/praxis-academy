from decimal import DivisionUndefined
from inspect import ClassFoundException
from tkinter import Y
from trace import Trace


try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  
  def bool_return():
    try:
        return True
    finally:
        return False
bool_return()
def divide(x, y)
    try:
        result = x / y
except ZeroDivisionError:
    print("division by zeroo!")
else:
    print("result is", result)
    finally:
        print("executing finallly clause")

divide(2, 1)
result is 2.0
executing finally clause
divide(2, 0)
division by zero!
executing finally clause
divide("2", "1")
executinng finally clause
Traceback (most recent call last):
file "<stdin>", line 1, in <module>
file "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for / : 'str' and 'str'