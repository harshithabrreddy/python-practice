n=int(input("Enter  the value  of n:"))
rev,rem=0,0
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
    print(f"Reversed number is{rev}")