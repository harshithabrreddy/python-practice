num = int(input("Enter an integer: "))

# Check if the number is a three-digit number or not
if (num >= 100 and num <= 999) or (num <= -100 and num >= -999):
    print(f"{num} is a three-digit number.")
else:
    print(f"{num} is not a three-digit number.")
