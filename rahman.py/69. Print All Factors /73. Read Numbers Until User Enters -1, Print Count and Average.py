count = 0
sum = 0

while True:
    n = float(input("Enter a number (-1 to stop): "))

    if n == -1:
        break

    sum += n
    count += 1

if count > 0:
    average = sum / count

    print("Count =", count)
    print("Average =", average)
else:
    print("No numbers were entered")
