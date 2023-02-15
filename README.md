# LAB - Class42

## Project: Pythonisms

Author: Don Choi

## Description

**Using iterators/generators on a custom collection**  

It allows users to add items to it using the "add_item" method. We then define the "iter" method which returns an iterator over the items in the collection, and the "len" method which returns the length of the collection. With these methods, we can use the custom collection in a for loop, a list comprehension, or convert it to a list.

**Creating a decorator that adds behavior to a given function**

It takes a function as input, and returns a new function that adds timing functionality to the original function. The new function is called a "wrapper" function, which calls the original function and calculates the time taken to execute it. We then use the decorator to decorate a function called "my_function" which adds a delay of 1 second, and call it to see the timing information.

**Using dunder methods to make custom data structures more elegant**

It takes a list of data as input. We then define the "eq" method which compares the data of two instances of the class, and the "bool" method which determines whether an instance is truthy or falsy. With these methods, we can compare two instances for equality using the "==" operator, and determine whether an instance is truthy or falsy using the "if" statement.
