def count_digits(number):
    count = 0
    while number != 0:
        number //= 10
        count += 1
    return count

def find_smallest_and_highest_digits(number):
    smallest = 9
    highest = 0
    while number != 0:
        digit = number % 10
        if digit < smallest:
            smallest = digit
        if digit > highest:
            highest = digit
        number //= 10
    return smallest, highest

number = int(input("Please enter an integer: "))

num_digits = count_digits(number)

smallest_digit, highest_digit = find_smallest_and_highest_digits(number)

print("Number of digits in the given number is:", num_digits)
print("Smallest number is:", smallest_digit)
print("Highest number is:", highest_digit)