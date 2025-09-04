# Chapter 2 Exercise Set 0: Chapter Review

## Asking Python for Datatype

### Use the type(...) command to determine the type of each of the following:

	42 = int

        4.2 = float

        ‘42’ = str
 
        4, 2 = TypeError, too many arguments, only takes 1 or 3.

### Now repeat the same process (using type(...)) and note what you get from each of the following:

        type(3 + 6) = int

        type(‘3 + 6’) = str

        type(True) = bool

        type([1, 2, 3]) = list 

        type((1, 2, 3)) = tuple

## The input function

### Describe in your own words how what the input function does, and how it works.

The input function is a function which can be added to a variable for a prompt to get information from the user.

### Look at the following Python REPL session:

num = input("Please enter a number between 1 and 10: ")

type(num)

### How will the Python interpreter respond? Explain why.

The Python interpreter will tell the user that is is a string. This is because the input function always returns the value as a string value which  can be converted afterwards.

## Converting between types

### Type each of the following into the Python REPL and think about what you see:

int('17')
=results with 17

type(int('17'))
=tells us it results with an integer

str(17)
=results with '17'

type(str(17))
=tells us it results with a string

### What to you think will happen when you enter the following? Think about it before you try it!

int('3 + 6')

### Did you get what you expected? Why or why not?
No, I was expecting a interger of 9. Instead I got a error due to it being an invalid literal. 

## All work and no play

### Take the sentence: All work and no play makes Jack a dull boy. Store each word in a separate variable, then print out the sentence on one line using print.

done.

## Order of operations

### Add parenthesis to the expression 6 * 1 - 2 to change its value from 4 to -6.
6*(1-2)

## Adding a comment

### Place a comment before a line of code that previously worked, and record what happens when you rerun the program.
The line of code becomes part of the comment and does not appear.

## NameError

###  Start the Python interpreter and enter bruce + 4 at the prompt. This will give you an error:

    NameError: name 'bruce' is not defined

    Assign a value to bruce so that bruce + 4 evaluates to 10.
: bruce= 6

## “Hello, Bob!”

### Write a program in a file named hello_bob.py that will produce a session something like this:

    $ python3 hello_bob.py

    Hi there! What's your name? Susmita

    Well, I'm pleased to meet you, Susmita!

    $

done!

## An n year old who likes x

### Write a program in a file named n_year_old.py that will produce a session something like this:

    $ python3 n_year_old.py

    How old are you? 16

    What is your favorite food? spam

    Ah, a 16 year old who likes spam.  How interesting!

    $

done!

## Compound interest

### The formula for computing the final amount if one is earning compound interest is
 
it didnt copy over.

###    Write a Python program that assigns the principal amount of $100 to variable p, assigns to n the value 12, and assigns to r the interest rate of 8% (as a float). Then have the program prompt the user for the number of years, t, for which the money will be compounded. Calculate and print the final amount after t years.

    Tip

    Remember to use type converter functions to turn the strings returned by the input function into numbers.



## What school?

###  Write a program in a file named what_school.py that will produce a session something like this:

    $ python3 what_school.py

    What is your name? Miguel
    How old are you, Miguel? 17
    Excellent! 17 is a great age to be.
    What school do you attend, Miguel? NVCC
    A fine school, NVCC.

    $


