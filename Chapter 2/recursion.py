def factorial_it(n): # Iterative version
    the_product = 1
    while n > 0:
        the_product *= n
        n = n - 1
    return the_product

print(factorial_it(5))

def factorial_recursive(n): # Recursive version
    if (n == 0):
        return 1
    return n * factorial_recursive(n - 1)


print(factorial_recursive(5))