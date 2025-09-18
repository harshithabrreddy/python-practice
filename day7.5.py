num=[1,2,3,4,5,6,7,8,9,10]
res=[]
for i in num:
    val=i+i
    res.append(val)
print(res)

#another logic  for double the sqaure numbs
num=[1,2,3,4,5,6,7,8,9,10]
res=[i+i for i in num]
print(res)

#double the square numbs by using map function
num=[1,2,3,4,5,6,7,8,9,10]
def double(n):
    return n+n
res=list(map(double,num))
print(res)
