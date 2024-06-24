def sum_of_digit(n):
    # Base Case
    if n < 10:
        return n
    # Recursive Case
    else:
        return n % 10 + sum_of_digit(n // 10)
print(sum_of_digit(12345))