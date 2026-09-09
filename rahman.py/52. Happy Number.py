n = int(input("Enter a number: "))

seen = set()

while n != 1 and n not in seen:
    seen.add(n)

    sum = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        sum += digit * digit
        temp //= 10

    n = sum

if n == 1:
    print("Happy number")
else:
    print("Not a happy number")
