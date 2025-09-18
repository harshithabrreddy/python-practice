#students grade in 3 subjects cal average marks,student passed or failed
Marks=tuple(map(int,input("Enter 3 Subjects marks:").split()))
avg=sum(Marks)/3
res=list(map(lambda i:i>=35,Marks))
res="Failed" if(False in res) else "Passed"
print(f"Average: {avg}")
print(res)