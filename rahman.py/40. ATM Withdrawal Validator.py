balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid withdrawal amount")

elif amount > balance:
    print("Insufficient balance")

elif balance - amount < 500:
    print("Withdrawal rejected")
    print("Minimum balance of 500 must be maintained")

else:
    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance =", balance)
