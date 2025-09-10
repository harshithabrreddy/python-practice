hours = float(input("Enter hours since you last drank water: "))

if hours >= 4:
    print("You are dehydrated! Drink water now!")
elif 2 <= hours < 4:
    print("Drink a glass of water")
else:
    print("You're fine")
