# Create two variables: a = 10 and b = 3.5
# Convert 'a' to a float and store it in a new variable
# Convert 'b' to an integer and store it in a new variable
# Print the original values and the converted values
# Use type() to print the type of each variable
# BONUS: Use a single print statement to print all variables in a formatted string

a = 10
b = 3.5

a_float = float(a)
b_int = int(b)

print(f"Original values:\n a: {a} (type: {type(a)})\n b: {b} (type: {type(b)})")
print(f"Converted values:\n a_float: {a_float} (type: {type(a_float)})\n b_int: {b_int} (type: {type(b_int)})")