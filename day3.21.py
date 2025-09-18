# Python program to find the second maximum number in a list
numbers = [10, 45, 3 , 7]
first_max = second_max = float('-inf')
for num in numbers:
    if num > first_max:
        second_max = first_max
        first_max = num
    elif num > second_max and num != first_max:
        second_max = num
print("Numbers in the list:", numbers)
if second_max == float('-inf'):
    print("No second maximum number found (list may have all elements equal).")
else:
    print("Second maximum number:", second_max)