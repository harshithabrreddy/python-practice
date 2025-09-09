num = int(input("Enter an integer: "))

# Check if the number is a four-digit number or not
if (num >= 1000 and num <= 9999) or (num <= -1000 and num >= -9999):
    print(f"{num} is a four-digit number.")
else:
    print(f"{num} is not a four-digit number.")