n = int(input("Enter number of elements: "))

a = []

for i in range(n):
    a.append(int(input("Enter element: ")))

for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if a[j] < a[min_index]:
            min_index = j

    a[i], a[min_index] = a[min_index], a[i]

print("Sorted list:", a)
