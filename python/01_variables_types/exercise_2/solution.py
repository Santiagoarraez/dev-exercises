#Solution (remenber it is just an example, you can solve it in different ways)

a = 10
b = 3.5

a_float = float(a)
b_int = int(b)

print(a)
print(b)

print(a_float)
print(b_int)

print(type(a))
print(type(b))
print(type(a_float))
print(type(b_int))

#Bonus (Use a single print statement to print all variables in a formatted string)

print(f"Original values:\n a: {a} (type: {type(a)})\n b: {b} (type: {type(b)})")
print(f"Converted values:\n a_float: {a_float} (type: {type(a_float)})\n b_int: {b_int} (type: {type(b_int)})")