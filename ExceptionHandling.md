# 1. Exception Handling

## Try & Except

-  The try block raises an error, the except block will be executed.
-  Without the try block, the program will crash and raise an error.

```python
    try:
      print(x)
    except:
      print("An exception occurred")   

    #output
    An exception occurred
```

## Many Except

-  You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error

```python
    try:
      print(x)
    except NameError:
      print("Variable x is not defined")
    except:
      print("Something else went wrong")   

    #output
    Variable x is not defined
```

## Else

- You can use the else keyword to define a block of code to be executed if no errors were raised

```python
    try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#output 
Hello
Nothing went wrong
```

## Finally

- The finally block, if specified, will be executed regardless if the try block raises an error or not.

```python
    try:
      print(x)
    except:
      print("Something went wrong")
    finally:
      print("The 'try except' is finished")
    #output
    Something went wrong
    The 'try except' is finished
```

## Raise an exception

- As a Python developer you can choose to throw an exception if a condition occurs.
- To throw (or raise) an exception, use the `raise` keyword.


```python
try:
    x = "hello"
    if not type(x) is int:
        raise TypeError
except TypeError as e:
    print("Different datatype")

    #output
    Different datatype
```

# 2. Built-in Exceptions

## ArithmeticError Exception

- Handling the ArithmeticError in a try...except statement:

```python
    try:
        print(10 / 0)
    except ArithmeticError:
        print("Error in calculation")
    except:
        print("Something else went wrong")
    #output
    Error in calculation
```
## OverflowError Exception

- If a mathematic function gets a too large number, it raises a OverflowError.

```python
    import math
    try:
        print(math.exp(999))
    except OverflowError:
        print("The number is too high")
    except:
        print("Something else went wrong")
    #output
    The number is too high

```

## ZeroDivisionError Exception

- The ZeroDivisionError exception occurs when you try to devide a number with 0, and when you perform a modulo operation with 0.

```python
    try:
      print(10 / 0)
    except ZeroDivisionError:
      print("Error in calculation")
    except:
      print("Something else went wrong")
    #output
    Error in calculation

```

## FloatingPointError Exception

- In Python are approximations of real numbers, leading to rounding errors, loss of precision, and cancellations that can throw off calculations.

## AssertionError Exception

- The AssertionError exception occurs when an assert statement fails.

```python
x = "hello"
try:
  assert x == "goodbye"
except AssertionError:
  print("Error in assert statement")
except:
  print("Something else went wrong")

#output
Error in assert statement

```

## AttributeError Exception

- The AttributeError exception occurs when you try to execute a property or method that does not exist on the current object.

```python
x = "Hello"
try:
    print(x.toUpperCase())
except AttributeError:
    print("Oops! Strings do not have a toUpperCase method!")
except:
    print("Something else went wrong")

#output
Oops! Strings do not have a toUpperCase method!

```

## ValueError Exception 

- The ValueError exception occurs if a function receives a value of wrong type.

```python
try:
  x = float("hello")
except ValueError:
  print("The value has wrong format")
except:
  print("Something else went wrong")

#output
The value has wrong format

```

## TypeError Exception 

- The TypeError exception occurs if an operation tries to perform an action with an unexpected data type.

```python
try:
  x = "hello" + 15
except TypeError:
  print("Please convert to string before concatenate")
except:
  print("Something else went wrong")
#output
Please convert to string before concatenate
```

## NameError Exception 

- The NameError exception occurs if you use a variable that is not defined

```python
try:
  print(x)
except NameError:
 print("Variable x is not defined")
except:
 print("Something else went wrong")
#output
Variable x is not defined
```

## KeyError Exception 

- The KeyError exception occurs when you use a key on a dictionary, and the key does not exist.

```python
fruit = {"name": "apple", "color": "red"}
try:
  print(fruit["price"])
except KeyError:
  print("You are trying to access a dictionary item that does not exist!")
except:
  print("Something else went wrong")
#output
You are trying to access a dictionary item that does not exist!
```

## IndexError Exception 

- The IndexError exception occurs when you use an index on a sequence, like a list or a tuple, and the index is out of range.

```python
x = ["apple", "banana", "cherry"]
try:
  print(x[5])
except IndexError:
  print("You are trying to access an item that does not exist!")
except:
  print("Something else went wrong")
#output
You are trying to access an item that does not exist!
```

# 3. User-defined Exception

-  Python provides many built-in exceptions, sometimes we may need to create our own exceptions to handle specific situations that are unique to application.
  
```python
class InvalidAgeError(Exception):
    def __init__(self, age, msg="Age must be between 0 and 120"):
        self.age = age
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.age} -> {self.msg}'

def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    else:
        print(f"Age set to: {age}")

try:
    set_age(150)  # This will raise the custom exception
except InvalidAgeError as e:
    print(e)

#output
150 -> Age must be between 0 and 120
```