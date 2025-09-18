# Program to print next 25 leap years
year = int(input("Enter a year: "))
count = 0
print("The next 25 leap years are:")
while count < 25:
    year += 1  # check from the next year onwards
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year)
        count += 1