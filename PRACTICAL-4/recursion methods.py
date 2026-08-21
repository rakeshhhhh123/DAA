def im(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * im(n - 1)
n = int(input("Enter a number: "))
print("Factorial =", im(n))
