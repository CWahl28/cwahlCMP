# a function to test if an interger is even.
def is_even(n):
    """
    >>> is_even(2)
    True
    >>> is_even(5)
    False
    >>> is_even(18)
    True
    """
# these are the example doctests made for this function.
    if int(n) % 2 == 0:
# the modulus operator is used on 'n' with 2, and checks if the result is equivalent to 0. 
# if it is equivalent to 0, it returns the word True. 
        return True
    else:
# if it is not equivalent to 0, it returns the word False. 
        return False

# a function to test if an interger is odd.
def is_odd(n):
    """
    >>> is_odd(3)
    True
    >>> is_odd(16)
    False
    >>> is_odd(15)
    True
    """
# the example doctest made for this function.
    if int(n) % 2 != 0:
#the modulus operator is used on 'n' with 2, and checks if the result is NOT equivalent to 0.
# if it is not equivalent to 0, it will return the word True. 
        return True
    else:
# if it is equivalent to 0, it will return the word False.
        return False

# a function to test if an interger is odd using the previous is_even function.
def even_odd(n):
    """
    >>> even_odd(14)
    False
    >>> even_odd(17)
    True
    >>> even_odd(3)
    True
    """
# the example doctests made for this function.
    if is_even(n) == True:
# the if statement calls is_even with 'n' and evaluates the result.
# if the result is equivalent to True, it will return with False as the interger is proven to be true by the is_even function. 
        return False
    else:
# if the result is equivalent to anything other than True, it will return with True, as the interger is proven not true.
        return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
