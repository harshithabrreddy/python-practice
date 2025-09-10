account_balance = 5000

# Customer enters withdrawal amount
withdraw = int(input("Enter withdrawal amount: "))
#if elif else
if withdraw > account_balance:
    print("Insufficient balance")
elif withdraw % 100 != 0:
    print("Amount should be multiple of 100")
else:
    account_balance -= withdraw
    print(f" Withdrawal successful! Remaining balance: ₹{account_balance}")
