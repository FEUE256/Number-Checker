from math import isqrt

# Kontrollera perfekt kvadrat
def is_perfect_square(n):
    root = isqrt(n)
    return root * root == n

# Kontrollera Fibonacci
def is_fibonacci(n):
    return is_perfect_square(5*n**2 + 4) or is_perfect_square(5*n**2 - 4)

# Hitta Fibonacci-index (F0=0)
def find_fibonacci_index(n):
    a, b = 0, 1
    index = 0
    while a < n:
        a, b = b, a + b
        index += 1
    if a == n:
        return index
    return None

# Kontrollera primtal (för små tal)
def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    r = isqrt(n)
    for i in range(3, r+1, 2):
        if n % i == 0:
            return False
    return True

# Hitta index i primtalsserien (praktiskt bara för små tal)
def find_prime_index(n):
    if not is_prime(n):
        return None
    count = 0
    candidate = 2
    while candidate <= n:
        if is_prime(candidate):
            count += 1
        if candidate == n:
            return count
        candidate += 1
    return None

# Dynamiskt input
x_str = input("Enter a number to check: ")
x = int(x_str)

print(f"Number to check: {x}")

fib = is_fibonacci(x)
print(f"Is Fibonacci: {fib}")
if fib:
    print(f"Fibonacci index (F0-based): {find_fibonacci_index(x)} (+1)")

prime = is_prime(x)
print(f"Is prime: {prime}")
if prime:
    print(f"Prime index: {find_prime_index(x)}")

print("Press Enter to continue...")
input()  # Väntar tills användaren trycker Enter
