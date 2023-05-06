for num in range(1, 100):
    if num <= 9:
        print("0", end="")
    print(num, end="")
    if num != 99:
        print(", ", end="")
