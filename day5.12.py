#check whether it is prime palindrome or not
num = int(input("Enter a number: "))
prime = True
if num <= 1:
    prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
original = str(num)         # convert number to string
reverse = original[::-1]    # reverse the string
if original == reverse:
    palindrome = True
else:
    palindrome = False
if prime and palindrome:
    print(num, "is a Prime Palindrome number.")
else:
    print(num, "is NOT a Prime Palindrome number.")
