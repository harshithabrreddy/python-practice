num = int(input("Enter an integer: "))

# Check if the number is a two-digit number
if num >= 10 and num <= 99 or num <= -10 and num >= -99:
    print(f"{num} is a two-digit number.")
else:
    print(f"{num} is not a two-digit number.")
