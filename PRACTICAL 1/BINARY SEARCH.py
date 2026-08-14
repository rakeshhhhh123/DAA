numbers = [ 5, 6, 7, 8, 9]

key = int(input("Enter the number to search: "))

low = 0
high = len(numbers) - 1

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == key:
        print("Number found at index", mid)
        break
    elif numbers[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Number not found")
