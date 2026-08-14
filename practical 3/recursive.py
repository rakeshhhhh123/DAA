def factorial_recursive(n):
   
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_recursive(n - 1)

n = 5
result = factorial_recursive(n)
print(f"Recursive Factorial of {n} is: {result}")
