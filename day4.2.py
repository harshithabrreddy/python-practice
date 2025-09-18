#Multiplication table of n using Functions
def table(n):
    print(f"Multiplication table of {n}/n")
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")
table(2)