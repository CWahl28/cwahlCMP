# Chapter 4 Exercise Set 0: Chapter Review

## Fix Quack and Ouack

###    Modify:

    prefixes = "JKLMNOPQ"
    suffix = "ack"

    for letter in prefixes:
        print(letter + suffix)

### so that Ouack and Quack are spelled correctly.

    for letter in prefixes:
        if letter == 'O':
            print(letter + 'u' + suffix)
        elif letter == 'U':
            print(letter + 'u' + suffix)
        else:
        print(letter + suffix)

YESSSS
this took me too long

## Remove a letter
 
###    Write a program named remove_a_letter.py that removes all occurrences of a given letter from a string.

###   A sample run of the program should look something like this:

    Enter a string: The rain in Spain falls mainly in the plain.
    Enter a letter to remove: i

    The ran n Span falls manly n the plan.

DONE

## Counting the number of a’s in a sentence

###    Write a program count_a.py that counts the number of times the letter a appears in a sentence.

###    A sample run of the program should look something like this:

    Enter a sentence: The rain in Spain falls mainly in the plain.

    The letter "a" appears in your sentence 5 times.

###    If there are no a’s in the sentence, it should simply say that:

    Enter a sentence: There is nothing here.

    The letter "a" does not appear in your sentence.

###    Finally, if there is only a single a the word, time, should be singular:

    Enter a sentence: Only happens once here.

    The letter "a" appears in your sentence 1 time.


DONEEE

## Modulus operator

###    Evaluate the following numerical expressions in your head, then use the Python interpreter to check your results:

        >>> 5 % 2
1 = yes
        >>> 9 % 5
4 = yes
        >>> 15 % 12
3 = yes
        >>> 12 % 15
error? = nope, 12, quotient is 0
        >>> 6 % 6
0 = yes
        >>> 0 % 7
0 = yes
        >>> 7 % 0
undefined = nope, ZeroDivisionError

###    What happened with the last example? Why? If you were able to correctly anticipate the computer’s response in all but the last one, it is time to move on. If not, take time now to make up examples of your own. Explore the modulus operator until you are confident you understand how it works.

Now more confident. :D

The last example specifically had a ZeroDivisionError because you cannot divide a number by zero. 

## Counting the length of sequences by traversal

###    Write a loop that traverses:

['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]

###    and prints the length of each element. What happens if you send an integer to len? Change 1 to 'one' and run your solution again.

done, turns out with error due to int and when changed prints amounts clearly.
results:
5
3
3
3

## Compute the sum

###    Study the following Python code.

    """Compute the sum of 1 + 2 + 3 + ... + n, and print the total."""
    n = int(input("Enter the number to which you want to sum: "))

    running_total = 0
    num = 1
    while num <= n:
        running_total = running_total + num
        num = num + 1

    print("The total is: ", running_total)

###    You can almost read the while statement as if it were English. It means, While num is less than or equal to n, continue executing the body of the loop. Within the body, add num to your running_total, then increment num. When num passes n, leave the loop and print your accumulated sum.

###    On paper, complete a trace of this program when n is assigned 6.

done

## Counting digits

###     The following program counts the number of decimal digits in a positive integer:

    n = int(input("Enter n: "))

    count = 0
    while n != 0:
        count = count + 1
        n = n // 10

    print(count)

###    Entering 710 for n will display 3. Trace the execution of this program to convince yourself that it works.

###    This program demonstrates an important pattern of computation called a counter. The variable count is initialized to 0 and then incremented each time the loop body is executed. When the loop exits, count contains the result — the total number of times the loop body was executed, which is the same as the number of digits.

###    If we wanted to only count digits that are either 0 or 5, adding a conditional before incrementing the counter will do the trick:

    n = int(input("Enter n: "))

    count = 0
    while n > 0:
        digit = n % 10
        if digit == 0 or digit == 5:
            count = count + 1
        n = n // 10

    print(count)

###    Confirm that you get 7 when you enter 1055030250 for n.
yup

###    Notice, however, that entering 0 for n will not give you 1. Explain why. Do you think this is a bug in the code?
It is not an error, as the code has n>0 as in the while statement, not >=, so it does not activate when n=0. 

## Invitations to a party

###    Write a program named lets_party.py that asks the user to enter a list of names and then prints out messages to each one of them inviting them to a party.

###    A sample run might go something like this:

    Enter invitee's name (or just enter to finish): Lucy
    Enter invitee's name (or just enter to finish): Sean
    Enter invitee's name (or just enter to finish): Chris
    Enter invitee's name (or just enter to finish): Delaine
    Enter invitee's name (or just enter to finish): Rachael
    Enter invitee's name (or just enter to finish): Antoan
    Enter invitee's name (or just enter to finish): Lary
    Enter invitee's name (or just enter to finish): Giselle
    Enter invitee's name (or just enter to finish):

    Lucy, please attend our party this Saturday!
    Sean, please attend our party this Saturday!
    Chris, please attend our party this Saturday!
    Delaine, please attend our party this Saturday!
    Rachael, please attend our party this Saturday!
    Antoan, please attend our party this Saturday!
    Lary, please attend our party this Saturday!
    Giselle, please attend our party this Saturday!

LETS GOOOO I DID IT

## Divisible by 2 or 3

###    Write a program that prints out each number from 2 to 20 and writes whether the number is divisible by 2 or 3, both, or neither. The output should look like this:

    Num   Div by 2 and/or 3?
    ---   ------------------
    2            by 2
    3            by 3
    4            by 2
    5            neither
    6            both
    7            neither
    8            by 2
    9            by 3
    10           by 2
    11           neither
    12           both
    13           neither
    14           by 2
    15           by 3
    16           by 2
    17           neither
    18           both
    19           neither
    20           by 2

Yippeeeee its done

## First multiple of 7

###    Write a program that traverses a list of numbers and prints out the first number in the sequence that is a multiple of 7 (hint: you may want to use a break statement for this) for the message, “No multiples of 7 found.” if none of the values in the list are multiples of 7.

Done!


