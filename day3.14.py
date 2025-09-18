#Arithmetic operations based on following conditions
a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
while(True):
 print("---operations menu-----")
 print("1.Addition")
 print("2.Substraction")
 print("3.Multiplication")
 print("4.Division")
 print("5.Exit")
 choice=int(input("Enter your choice:"))
 if(choice==1):
    print(f"Summation{a},{b}is{a+b}")
 elif(choice==2):
    print(f"Difference of{a},{b} is{a-b}")
 elif(choice==3):
    print(f"Product of{a},{b} is{a*b}")
 elif(choice==4):
    print(f"Quotient of{a},{b} is{a-b}")
 elif(choice==5):
    print("Thanks for using operations menu")
 break
