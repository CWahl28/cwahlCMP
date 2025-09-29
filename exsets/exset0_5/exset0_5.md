# Chapter 5 Exercise Set 0: Chapter Revew

## Dead Code

###    Write a function named my_dead_code that includes dead code.
done

## Exploring the math Module

###     Start a Python shell and type the following:

    import math

    dir(math)

### What do you see in the namespace of the math module? Write down the names of 10 of the items in the list look interesting to you. (ignore the ones that start and end with __ for now).



### Try out the following in the shell:

math.pi

type(math.pi)

type(math.log2)

print(math.log2.__doc__)

math.log2(32)

print(math.log.__doc__)

math.log(64)

math.log(64, 2)

math.log(64, 8)

type(math.isclose)

print(math.isclose.__doc__)

math.isclose(3.14, math.pi)

math.isclose(3.14159, math.pi)

math.isclose(3.141592653, math.pi)

###    Conduct similar “experiments” with the other items in your list to see what you can learn about them by using Python to explore.

## Encapsulating and Generalizing Our Guessing Game

###    Start with the guessing game example from the Conditionals, loops and exceptions chapter:

    import random                      # Import the random module 

    number = random.randrange(1, 1000) # Get random number between [1 and 1000)
    guesses = 0
    guess = int(input("Guess my number between 1 and 1000: "))

    while guess != number:
        guesses += 1
        if guess > number:
            print(guess, "is too high.") 
        elif guess < number:
            print(guess, " is too low.")
        guess = int(input("Guess again: "))

    print("\n\nGreat, you got it in", guesses,  "guesses!")

###    The first step in the encapsulation process is to wrap the programming logic in a function. Write a function named guess_game that runs the game when called with guess_game(). Put this in a file named guess1.py.

###    Copy guess1.py to guess2.py. Generalize the guess_game function in guess2.py to take two parameters: low, and high, such that a call to guess_game(100, 200) will begin with the message, “Guess my number between 100 and 200”.

## Getting Ready for TDD

### Create a file named ch5ex0.py for the exercises which follow. Put:

if __name__ == '__main__':
    import doctest
    doctest.testmod()

### at the bottom of the file.

### Use a test-driven development (TDD) approach to completing the each of the exercises by adding the doctests before you write code to make them pass.

## Encapsulation and Generalization Practice

###    The following program counts the number of times the digit 5 occurs in the number 1055030250:

    count = 0
    n = 1055030250

    while n > 0:
        digit = n % 10
        if digit == 5:
            count += 1
        n = n // 10

    print(count)

###    Wrap this logic in a function named count_digit(digit, number) and generalize it so it returns the number of times the digit, digit occurs in the number, number. It should pass the following doctests:

    def count_digits(digit, number):
        """
          >>> count_digits(5, 1055030250)
          3
          >>> count_digits(9, 909)
          2
          >>> count_digits(7, 7777)
          4
          >>> count_digits(7, 1234)
          0
        """

## Composing sum and find_average

###    The built-in function sum returns the sum of a sequence of numeric values:

sum([5, 10, -15.5, 20])
19.5

    sum((1, 1, 1, 1))
    4

###    Use composition and the built-in sum function to write a function, find_average(nums), that returns the average of a sequence of numbers. It should pass the following doctests:

    def find_average(numbers):
        """
          >>> find_average([5, 10])
          7.5
          >>> find_average([5, 10, 15])
          10.0
          >>> find_average((1, 2, 2, 3))
          2.0
          >>> find_average([19])
          19.0
        """

## Transforming a List Two Ways

###    Write a function, only_evens(nums) that takes a list of integers as an argument and returns a list of only the even numbers in the same order in which they occured in the list argument:

    def only_evens(nums):
        """
          >>> only_evens([3, 8, 5, 4, 12, 7, 2])
          [8, 4, 12, 2]
          >>> my_nums = [4, 7, 19, 22, 42]
          >>> only_evens(my_nums)
          [4, 22, 42]
          >>> my_nums
          [4, 7, 19, 22, 42]
        """

###    Now write a function, keep_only_evens(nums) that modifies its parameter, removing odd numbers from the list.

    def keep_only_evens(nums):
        """
          >>> some_nums = [3, 8, 5, 4, 12, 7, 2]
          >>> keep_only_evens(some_nums)
          >>> some_nums
          [8, 4, 12, 2]
        """

## Mathematical Functions

###    Write Python functions that implement each of the following mathematical functions:

        g(x) = x 3 - 7

        h(x) = 2x 2 - 3x + 5

        k(x) = x 5 - 8x 3 + 7x - 11

###    These functions are simpler to write than the previous exercises, but you are expected here to make up your own tests before you write function bodies that make them pass.

## Challenge: find_median

###    Write a function named find_median that takes a list of numbers as an argument and returns the median of the numbers. You will need to find the precise definition of median, and write several doctests that cover the different cases involved in computing it.

## Challenge: find_mode

###    Write a function named find_mode that takes a list of numbers as an argument and returns the mode of the numbers. You will need to find the precise definition of mode, and write several doctests that cover the different cases involved in computing it.


