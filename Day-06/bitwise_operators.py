# Initial values
a = 10  # 1010 in binary
b = 4   # 0100 in binary

# Bitwise AND
and_result = a & b
print(f"Bitwise AND of {a} and {b} is {and_result} (binary: {bin(and_result)})")

# Bitwise OR
or_result = a | b
print(f"Bitwise OR of {a} and {b} is {or_result} (binary: {bin(or_result)})")

# Bitwise XOR
xor_result = a ^ b
print(f"Bitwise XOR of {a} and {b} is {xor_result} (binary: {bin(xor_result)})")

# Bitwise NOT
not_result = ~a
print(f"Bitwise NOT of {a} is {not_result} (binary: {bin(not_result)})")

# Bitwise left shift
left_shift_result = a << 2
print(f"Bitwise left shift of {a} by 2 positions is {left_shift_result} (binary: {bin(left_shift_result)})")

# Bitwise right shift
right_shift_result = a >> 2
print(f"Bitwise right shift of {a} by 2 positions is {right_shift_result} (binary: {bin(right_shift_result)})")