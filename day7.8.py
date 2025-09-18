#square values of list of elements without loop by using map function
num=list(map(int,input('Enter the numbers:').split()))
square=list(map(lambda i:i*i,num))
print(square)

#square values of list of elements with loop functions
size=int(input("Enter the size of list:"))
List=[]
New=[]
for i in range(size):
    val=int(input('Enter the value:'))
    List.append(val)
print(List)
for i in List:
    i=i*i
    New.append(i)
print(New)
