n=int(input("Enter the value of n:"))
rem,rev=0,0
temp=n
print(f"User Entered Number is{n}")
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
    print(f"Reversed number is{rev}")
    if(temp==rev):
        print("palindrome")
    else:
        print("Not a palindrome")