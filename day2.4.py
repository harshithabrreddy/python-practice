hours_worked = int(input("Enter the number of hours worked today: "))
# Standard work hours and overtime rate
standard_hours = 8
overtime_rate = 100
# if-else
if hours_worked > standard_hours:
    overtime_hours = hours_worked - standard_hours
    overtime_pay = overtime_hours * overtime_rate
    print("Overtime pay: ₹", overtime_pay)
else:
    print("No overtime pay")