"""
Put your tests here:

  >>> tricky[4]
  'this'
  >>> tricky[8]
  42
  >>> type(tricky[7])
  <class 'tuple'>
  >>> type(tricky[0])
  <class 'list'>
  >>> len(tricky)
  12

"""
# Put your solutions here:
tricky= [['zero'],1,2,3,'this',5,6,(7,'seven','IIV'),42,9,10,11]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
