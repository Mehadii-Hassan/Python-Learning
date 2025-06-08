#string indexing
#[start : end : step]
credit_number = "1234-5678-9012-3456"

print(credit_number[1]) #output - 2
print(credit_number[0:4]) #output - 1234
print(credit_number[:4]) #output - 1234
print(credit_number[5:9]) #output - 5678
print(credit_number[5:]) #output - 5678-9012-3456
print(credit_number[-1]) #output - 6
print(credit_number[::3]) #output - 146-136 (3 STEP)
print(credit_number[::-1]) #output - 6543-2109-8765-4321 (reverse)

last_four_digit = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_four_digit}")





