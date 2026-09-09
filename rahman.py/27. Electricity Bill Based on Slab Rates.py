units = float(input("Enter electricity units: "))

if units <= 100:
    bill = units * 1.50

elif units <= 200:
    bill = (100 * 1.50) + ((units - 100) * 2.50)

elif units <= 400:
    bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)

else:
    bill = (100 * 1.50) + (100 * 2.50) + (200 * 4.00) + ((units - 400) * 6.00)

print("Electricity bill = ₹", bill)
