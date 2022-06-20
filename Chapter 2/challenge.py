def print_number_until_it(n): # Iterative version
    x = 0
    while(x <= n):
        print(x)
        x = x + 1
    
    return

def print_number_until_recursive(n): # Recursive version
    if (n > 0):
        print_number_until_recursive(n - 1)
        print(n)

    return

print_number_until_it(10)
print_number_until_recursive(10)