"""
  >>> type(this)
  <class 'str'>
  >>> type(that)
  <class 'int'>
  >>> type(something)
  <class 'float'>
"""
this= "twenty-five"
that= 25
something= 2.5

if __name__ == '__main__':
    import doctest
    doctest.testmod()
