num=int(input('Enter the integer:'))
#if-else
if(num>=-9 and num<=9):
    print("Digit")
else:
    print("Number")
#ternory operator
res="Digit" if (num>=-9 and num<=9) else "Number"
print(res)