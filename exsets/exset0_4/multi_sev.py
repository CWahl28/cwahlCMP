for i in [13, 16, 80, 74, 22, 57]:
    if i % 7 != 0:
        continue
    print(i)
    break
else:
    print("No multiples of 7 found.")
