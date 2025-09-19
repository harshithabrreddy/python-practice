#Enter the value of n:3
#     1
#   1 2
# 1 2 3
n=int(input('Enter the value of n:'))
for i in range(1,n+1):
  for j in range(1,n+1):
    print(f"  {j}")
  print()
