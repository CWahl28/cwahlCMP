"""
Put your tests here:

  >>> whatsthis[2]
  42
  >>> type(whatsthis[4])
  <class 'list'>
  >>> whatsthis[6:8]
  [11, 'what is this?']
  >>> len(whatsthis)
  10

"""
# Put your solutions here:
whatsthis = [1,2,42,3,['four'],5,11,'what is this?',9,10]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
