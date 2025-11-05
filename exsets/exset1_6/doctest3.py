words = input('Please enter a string: ')
amt = {}


def letter_count(words):
    words = words.lower
    for i in words:
        if i.isalpha:
            amt[i] = 0
        elif i in amt:
            amt[i] += 1
        else:
            continue
    return emt  
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
