# Chapter 3 Exercise Set 0: Chapter Review

## “Being the computer”

### Enter each of the following expressions into the Python REPL to see how Pyton evaluates it. You should anticipate what you will see before each one. When you can “be the computer” and correctly predict what you will see before you press enter, you will have learned.

    "NVCC CSC221"[5:8]
?= "CSC" = yes
    type([1, 'two', 3.0][1])
?= error? = nope, str
    'a' in 'apple'
?= yes/true = yes
    [1, 2, 3, 4, 5, 6][2:-1]
?= 3,4,5 = yes
    type(len('Mississippi'))
?= 11 = nope, class 'int'
    for i in 2, 4, 6, 8:
        print(i ** 2)
?= 4,16,36,64? = yea sorta
    3 > 2 and 1 > 2
?= false = yes
    not True or False
?= true? = nope, false
    not False and True
?= true = yes
    False and undefined_variable_name
?= false? = yes
    False or undefined_variable_name
?= true = nope, name error
### What will be the Python shell’s response to the following:

    thing = ['a', 'b']
    thing.append(['c', 'd'])
    thing

['a', 'b', ['c', 'd']]
yup

## Syntax and operations

### What is the result of each of the following?

###    Add a line between each line starting with a python prompt with the value that would appear when the given expression is evaluated.

    'Python'[1]
?= y = yea
    "Strings are sequences of characters."[5]
?= g = yea
    len("wonderful")
?= 9 = yea
    'Mystery'[:4]
?= Myst = yea
    'p' in 'Pineapple'
?= true =
    'apple' in 'Pineapple'
?= true = 
    'pear' not in 'Pineapple'
?= true = 
    (2, 4, 6, 8, 10)[1:4]
?= 4,6,8,10 = nope, 4,6,8
    [("cheese", "queso"), ("red", "rojo")][1][0][2]
?= Queso, cheese, red = nope, 'd'
got why: 1st tuple, 0th word, 2nd letter
### You’ll need to become familiar with the different methods of each type to do these.

    'Python'.upper()
?= PYTHON = yes
    'Mississippi'.count('s')
?= 4 = yes
    letters = ['c', 'z', 'b', 's']
    letters.sort()
    letters
?= b,c,s,z = yes
    (3, 9, 8, 42, 17).index(42)
?= true = nope, tells place, 3
    "\t   \n     Don't pad me!   \n   \n".strip()
?= "Don't pad me!" = yes
    mystery = 'apples pears bananas cheesedoodles'.split()
    mystery
?= ['apples', 'pears', 'bananas', 'cheesedoodles'] = yes
    mystery.sort()
    mystery
?= ['apples', 'bananas', 'cheesedoodles', 'pears'] = yes
    mystery.reverse()
    mystery
?= ['pears', 'cheesedoodles', 'bananas', 'apples'] = yes
### What value will appear after these two lines are entered at the prompt?

    word = "Pneumonoultramicroscopicsilicovolcanoconiosis"
    (word[6] + word[30] + word[33] + word[15]).upper()
?= NVCC = yes

## Logical opposites

### Give the logical opposites of these conditions

        a > b
a <= b
        a >= b
a < b
        a >= 18 and day == 3
a < 18 or day != 3
        a >= 18 and day != 3
a < 18 or day == 3
        3 == 3
3 != 3
        3 != 3
3 == 3
        3 >= 4
3 < 4
        not (3 < 4)
3 < 4

## Four friends and a movie

###  Write a program in a file named movie_friends.py that will produce a session something like this:

    $ python3 movie_friends.py

    Hmmm... You have 5 tickets to that new movie everyone wants to see.
    Whom should you invite to go with you?

    Enter the name of friend one: Sean
    Your invite list now contains: ['Sean']

    Enter the name of friend two: Jonathan
    Your invite list now contains: ['Sean', 'Jonathan']

    Enter the name of friend three: Margot
    Your invite list now contains: ['Sean', 'Jonathan', 'Margot']

    Enter the name friend four: Justin
    Your invite list now contains: ['Sean', 'Jonathan', 'Margot', 'Justin']

    Great!  You are ready to go to the movie...

    $

done.

## What is is

###  What will be the output of the following program?

    this = ['I', 'am', 'not', 'a', 'crook']
    that = ['I', 'am', 'not', 'a', 'crook']
    print("Test 1:", this is that)
    that = this
    print("Test 2:", this is that)

test one, false? = yes
test two, True? = yes
### Provide a detailed explaination of the results.
Test one results in false, as while the two lists are technically the same in contents, they have not yet been set to actually be equal. 
The "this = that" in between the tests sets the two things to be set as aliases of one another, and offically the same.
Due to the action inbetween, the second test results in true, as they are now equal. 

## What are you learning?

###  Write a program in a file named learning_what.py that will produce a session something like this:

    $ python3 learning_what.py

    So, tell me one thing you are learning in that course: HTML
    Your list of skills now contains: ['HTML']

    Name another thing you are learning: CSS
    Your list of skills now contains: ['HTML', 'CSS']

    And another: Python
    Your list of skills now contains: ['HTML', 'CSS', 'Python']

    Wow!  I should take that class too.

    $

done.

## More syntax and operations

### How would the Python interpreter respond to each of the following if it was entered at the Python prompt?

        'NVCC Rocks!'[5]
R = yes
        "Strings are sequences of characters."[-2]
s = yes
        len("What's all this then? Amen!")
27 = yes
        'Mystery'[:4]
Myst = yes
        'x' in 'Aardvark'
false = yes
        'pin' in 'Pinapple'
true = nope, capitalization
        'a' not in 'Pinapple'
false = yes
        (2, 3, 5, 7, 11, 13, 17)[-3:]
11, 13, 17 = yes
        [("cheese", "red", "sing"), ("queso", "red", "cantar")][0][2][0]
s = yes

### You’ll need to become familiar with the different methods of each type to do these.

        'Python'.upper()
PYTHON = yes
        'We are all in this together!'.count('e')
4 = yes
        (2, 3, 5, 7, 11, 13, 17, 19, 23).index(7)
3 = yes
        "\t   \n     Just the facts, mam!   \n   \n".strip()
'Just the facts, mam!' = yes
###  What will the Python shell print out for numbers in the following shell session?

    numbers = [11, 7, 42, -3, 0, 18]
    numbers.sort()
    numbers

-3,0,7,11,18,42 = yes

### What will the Python shell print out for nomystery each time it is entered in the following shell session?

    nomystery = "These are the times that try men's souls".split()
    nomystery
['These','are','the','times','that','try',"men's",'souls'] = yes!

    nomystery.sort()
    nomystery
These, are, men's, souls, that, the, times, try = yes!

    nomystery.reverse()
    nomystery
try, times, the, that, souls, men's, are, These = yes!


