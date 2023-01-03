"""
Function Object:

In Python functions are objects just like integers, strings, lists... etc.

Function objects are often used for event handling, but are also useful for adding the ability to
extend behaviour. For example, they are commonly used in the popular web framework Wordpress to create
"hooks" that plugin developers can "hook" into to insert their own custom code.

Let's have a look at this feature. I recommend following along using the Python Console so that you
can experiment and see the outputs.

Consider the following, then copy and paste it into the Python Console:
"""


def do_thing(value):
    print(value + 1)


do_thing(5)  # output: 6

"""
So far so good. That's how we normally call a function.
But what is the output if we do this?:
"""

x = do_thing
x(5)

"""
Notice that do_thing doesn't have any brackets after it.
Instead, the brackets are used in the next line.

The output of x(5) is 6. But why?
Let's have another look at the code: 
"""

x = do_thing  # the function do_thing is assigned to variable x.
print(type(x))  # output: <class 'function'>
print(x)  # output: <function do_thing at ...>  (i.e. a 'function' object that refers to the function do_thing)

x(5)  # Calls function do_thing with the argument 5. It is the same as calling do_thing(5).

"""
As you can see x is a variable that refers to the function do_thing.
We can call x with arguments as if it were a function. 
It uses those arguments to call the function that it refers to, i.e. do_thing.
"""

y = x  # We can assign another variable that refers to the function do_thing.
x(10)  # output: 11
y(10)  # output: 11

"""
Consider the following:
"""


def calculate_thing(a, b):
    return a * b


y = calculate_thing  # We can assign a different function to y.
result = y(3, 4)  # Now y refers to the function calculate_thing(), which takes in two arguments.
print(result)  # output: 12

"""
Question: What happens if we try to call x(2, 3)?
"""

result = x(2, 3)
print(result)

"""
The arguments must match the parameters of the function that x refers to.
x refers to do_something(), which only takes 1 argument, not 2. 

We can also have function objects that have no parameters.
"""


def say_hi():
    print("hi")


x = say_hi
x()  # Output: hi

"""
So we can now see how to store functions in variables, but we can also use them as function arguments.
For instance, what will the output of the following be?: 
"""


def perform_action(action):
    action()


perform_action(x)

""" 
We can see that x refers to the function say_hi. It is passed in as an argument to perform_action().
The parameter action then refers to say_hi.
We do the following:
    action()
Which is equivalent to:
    say_hi()

What would happen if we mistakenly used brackets after x instead? 
"""

perform_action(x())

"""
As the error message points out we are trying to call None.
Why would x() be None? 

Consider the following further example that uses y from above (calculate_thing):
"""


def display_result(operation):
    result = operation()
    print(result)


display_result(y(2, 3))

"""
Now the error is that the type 'int' is not callable.
So if y(2, 3) is the same as calculate_thing(2, 3) then that evaluates to 6.
Then we are calling display_result(6).
Inside the display_result function we call
    operation()
Where operation refers to y, which is 6.
Try to run the following code in the Python console and you'll get 'int' is not callable error.
"""

6()

"""
We could try to fix that by not using brackets:
"""

display_result(y)

"""
Now we get a different error. This time, that we are missing 2 required position arguments, a and b.
Inside display_result we call
    operation()
Which evaluates to
    y()
y refers to calculate_thing, which requires 2 arguments (a and b).
So we need to use the correct arguments.
We could do the following to resolve the error.
"""


def display_result(operation, a, b):
    result = operation(a, b)
    print(result)


display_result(y, 2, 3)

"""
You might be wondering how this could be useful, when we could simply call a function
directly. Consider the following:
"""


def customisable_function(a, b, operation):
    """
    Return the result of a custom operation on a and b.
    Operation is a function object that is called with arguments (a, b).
    """
    return operation(a, b)


def my_custom_operation(a, b):
    """Perform modulo of a and b."""
    return a % b


result = customisable_function(6, 5, my_custom_operation)  # Remember not to use brackets after my_custom_operation.
print(result)  # Output: 1

"""
This is a flexible approach that has the following advantages:
1. We can create new operations without having to modify customisable_function.
2. customisable_function is simple and easy to read, even if we add a large number of custom operations.
3. customisable_function can live in a different file (module) than my_custom_operation. 
This helps separate interface from implementation, and helps with teamwork.
4. We can easily add many functions this way.

There is a limitation, as shown in the above exercise:
We have to use the same parameters. For example, if we wanted to add an operation that took an extra
parameter it would fail when we tried to call customisable_function.
For example: 
"""


def my_advanced_operation(a, b, factor):
    """Return a + b, multiplied by a factor."""
    return (a + b) * factor


result = customisable_function(2, 3, my_advanced_operation)
print(result)

"""
We'll see a more expanded example in the next file, custom_input_handlers.py.
For now, consider how this might help apply to our problem of needing to
allow users of our function to customise how the function behaves.

Note: You may want to research the term "callback function". 
It is a commonly used synonym for "function object".
"""
