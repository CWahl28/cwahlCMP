for i in range(2,21):
    if i % 2 == 0 and i % 3 == 0:
        print(i, "      both")
    elif i % 3 == 0:
        print(i, "      by 3")
    elif i % 2 == 0:
        print(i, "      by 2")
    else:
        print(i, "      neither")
             
