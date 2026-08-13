n = int(input("Enter number of elements: "))

a = []

for i in range(n):
    a.append(int(input("Enter element: ")))

size = 1

while size < n:
    for left in range(0, n, 2 * size):
        mid = min(left + size, n)
        right = min(left + 2 * size, n)

        temp = []
        i = left
        j = mid

        while i < mid and j < right:
            if a[i] < a[j]:
                temp.append(a[i])
                i += 1
            else:
                temp.append(a[j])
                j += 1

        while i < mid:
            temp.append(a[i])
            i += 1

        while j < right:
            temp.append(a[j])
            j += 1

        for k in range(len(temp)):
            a[left + k] = temp[k]

    size *= 2

print("Sorted list:", a)

