def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Please enter a positive integer: "))
result = sum_of_numbers(n)
print("The sum of numbers from 1 to", n, "is:", result)