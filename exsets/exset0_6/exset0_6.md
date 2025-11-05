# Chapter 6 Exercise Set 0: Chapter Review

## Dictionary Operations

###    Give the Python interpreter’s response to each of the following from a continuous interpreter session:

d = {'apples': 15, 'bananas': 35, 'grapes': 12}

d['bananas']
35

d['oranges'] = 20

len(d)
4

'grapes' in d
True

'kiwis' in d
False

d.get('apples', 0)
15

d.get('pears', 0)
0

d2 = {(3, 2): 15, (1, 3): 35, (7, 4): 12, (6, 1): 42, (5, 5): 19}

d2[(7, 4)]
12

del d2[(1, 3)]

len(d2)
4

d2.get((6, 1), 0)
42

d2.get((4, 10), 0)
0

###   Be sure you understand why you get each result.
done

## Fruit Inventory

###   Apply what you have learned in the previous exercises to fill in the body of the function below:

    def add_fruit(inventory, fruit, quantity=0):
        """
        Adds quantity of fruit to inventory.

           >>> new_inventory = {}
           >>> add_fruit(new_inventory, 'strawberries', 10)
           >>> 'strawberries' in new_inventory
           True
           >>> new_inventory['strawberries']
           10
           >>> add_fruit(new_inventory, 'strawberries', 25)
           >>> new_inventory['strawberries']
           35
         """

###    Your solution should pass the doctests.
i did it :D

## Hello File!

###    Use Python to create a file named hello_file.txt with text that reads:

    Hello, this is [name] here, writing in a text file with Python!

    with your name substituted for [name].


## List From a File

###    Write a Python program that opens a file named list.txt containing a list of items, one per line, reads in the data, and turns them into a Python list. For example, if list.txt contains:

    this
    that
    stuff
    such

###    Your program should create the python list:

    ['this', 'that', 'stuff', 'such']

## Numbers From a File

###    Write a Python program that opens a file named numbers.txt containing a list of integers, one per line, reads in the data, and turns them into a Python list. For example, if numbers.txt contains:

    13
    97
    42
    17
    11

###    Your program should create the python list:

    [13, 97, 42, 17, 11]


