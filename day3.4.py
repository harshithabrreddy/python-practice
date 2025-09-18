n=int(input("Enter the value of n:"))
even,odd,rem=0,0,0
while(n!=0):
    rem=n%10
if rem%2==0:
    even+=1
else:
    odd+=1
    n=n//10
    print(f"Even Digit count is{even}")
    print(f"Odd Digit count is{odd}")