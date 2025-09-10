bill = float(input("Enter the total bill amount: ₹"))

# Apply discount based on conditions
if bill > 500:
    discount = 0.10 * bill   # 10% discount
elif bill > 100:
    discount = 0.05 * bill   # 5% discount
else:
    discount = 0             # No discount

# Calculate final amount
final_amount = bill - discount

# Display results
print(f"Original Bill: ₹{bill:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Final Amount to Pay: ₹{final_amount:.2f}")
