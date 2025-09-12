# Chapter 3 Exercise Set 2: PCEP Practice

## The == operator

### Evaluate each of the following expressions:

        42 == 42

        42 == 42.

        42 == 43

## Other comparision operators

### Evaluate each of the following expressions:

        42 != 42

        42 > 42.

        42 < 43

## Updated Precedence Table

Priority        Operator
1               +, -            unary
2               **
3               *, /, //, %
4               +, -            binary
5               <, <=, >, >=
6               ==, !=
	
## Challenge: Greater than?

### Using one of the comparison operators in Python, write a simple two-line program that takes the parameter n as input, which is an integer, and prints False if n is less than 42, and True if n is greater than or equal to 42.

## Dictionary Preview

### In the Dictionaries, sets, files and modules chapter you will learn about Python’s dictionary data type. We’ll introduce a “sneak preview” here, since many PCEP questions require you to recognize a dict when you see one, and it will be helpful to introduce those questions now.

my_dictionary = {}

type(my_dictionary)
<class 'dict'>

my_dictionary['key1'] = 'value'

my_dictionary['key2'] = 42

print(my_dictionary)
{'key1': 'value1', 'key2': 42}

### You can recognize Python dictionaries by these two characteristics:

1. They are enclosed in curly braces.

2.  They contain key-value pairs separated by commas, with the keys and values separated by colons (:).

