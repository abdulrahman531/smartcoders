n = int(input("Enter a number: "))

if n % 3 == 0 and n % 5 == 0:
    print("Number is divisible by both 3 and 5")
elif n % 3 == 0:
    print("Number is divisible by 3")
elif n % 5 == 0:
    print("Number is divisible by 5")
else:
    print("Number is divisible by neither 3 nor 5")
