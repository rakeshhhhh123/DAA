n = int(input("Enter number of elements: "))

a = []

for i in range(n):
    a.append(int(input("Enter element: ")))

stack = [(0, n - 1)]

while stack:
    low, high = stack.pop()

    if low < high:
        pivot = a[high]
        i = low - 1

        for j in range(low, high):
            if a[j] < pivot:
                i += 1
                a[i], a[j] = a[j], a[i]

        a[i + 1], a[high] = a[high], a[i + 1]

        p = i + 1

        stack.append((low, p - 1))
        stack.append((p + 1, high))

print("Sorted list:", a)
