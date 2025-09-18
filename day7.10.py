#shop records daily sales maximum sales in a single day,total slaes of the week
Sales=list(map(int,input('Enter the Sales for a week:').split()))
print(max(Sales))
print(sum(Sales))