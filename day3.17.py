# Python program to remove negative numbers from a list
numbers = [10, -3, 45, -20, 0, 67, -5, 89]
positive_numbers = [num for num in numbers if num >= 0]
print("Original list:", numbers)
print("List after removing negative numbers:", positive_numbers)