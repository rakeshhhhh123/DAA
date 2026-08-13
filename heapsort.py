n = int(input("Enter number of elements: "))

a = []

for i in range(n):
    a.append(int(input("Enter element: ")))

for i in range(n // 2 - 1, -1, -1):
    j = i

    while 2 * j + 1 < n:
        child = 2 * j + 1

        if child + 1 < n and a[child + 1] > a[child]:
            child = child + 1

        if a[j] < a[child]:
            a[j], a[child] = a[child], a[j]
            j = child
        else:
            break

print("Maximum:", a[0])

for i in range(n // 2 - 1, -1, -1):
    j = i

    while 2 * j + 1 < n:
        child = 2 * j + 1

        if child + 1 < n and a[child + 1] < a[child]:
            child = child + 1

        if a[j] > a[child]:
            a[j], a[child] = a[child], a[j]
            j = child
        else:
            break

print("Minimum:", a[0])
