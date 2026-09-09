x = float(input("Enter x: "))
n = int(input("Enter number of terms: "))

sum = 0
power = 1
factorial = 1
sign = 1

for i in range(n):
    # Calculate factorial of (2i + 1)
    term_number = 2 * i + 1

    factorial = 1
    for j in range(1, term_number + 1):
        factorial *= j

    term = (x ** term_number) / factorial

    sum += sign * term

    sign = -sign

print("Sum of the series =", sum)
