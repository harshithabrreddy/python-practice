#
string=input("Enter the string:")
alphabet,digit,specialchar=0,0,0
for ch in string:
    if ch.isalpha():
        alphabet+=1
    elif ch.isdigit():
        digit+=1
    else:
        specialchar+=1
    print(f"Count of alphabetic Characters is {alphabet}")
    print(f"Count of Digits is {digit}")
    print(f"Count of Special Characters is {specialchar}")