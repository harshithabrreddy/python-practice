#name to check the characters or not
name=input('Enter Your Name:')
char=input("Enter the character to check:")
if char in name:
    print(f"yes {char} is present in the name{name}")
else:
    print(f"no {char}is not present in the name{name}")

