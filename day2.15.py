salary = float(input("Enter your monthly salary (₹): "))
credit_score = int(input("Enter your credit score: "))

if salary >= 30000 and credit_score >= 700:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")