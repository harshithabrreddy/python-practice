age = int(input("Enter your age: "))
if age < 0:
    print(" Invalid age!")
elif age < 12:
    print("Ticket Price: ₹150 (Child)")
elif age <= 18:
    print(" Ticket Price: ₹200 (Teenager)")
else:
    print(" Ticket Price: ₹300 (Adult)")
