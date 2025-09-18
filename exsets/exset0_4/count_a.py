txt = input("Enter a sentance: ")
x = txt.count("a")


if x == 1:
    print("The letter 'a' appears in your sentance 1 time")
elif x == 0:
    print("The letter 'a' does not appear in your sentance.")
else:
    print("The letter 'a' appears in your sentance " + str(x) + " times.")
