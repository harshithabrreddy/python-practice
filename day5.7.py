#adhaar number where 1st digit written and the last 4 digits  being visible
adhaar = input("Enter your 12-digit Aadhaar number: ")
if len(adhaar) == 12 and adhaar.isdigit():
    masked = adhaar[0] + "*" * 8 + adhaar[-4:]
print("Masked Aadhaar Number:", masked)