# Logical Operator
# There are 3 types of logical operator
# and, or, not

# Logical operator returns boolean value(True/False)

# and operator

# All operands/expression must be true. If any of the expression is false
# then result will be false

x=12
y=4
z=8
print(x>y and x>z)
print(x>y and x<z and x==y and x!=z)


# or operator
# Any of the operands/expression must be true. If all of the expression is false
# then result will be false

print(x>y or x>z)
print(x<y or x<z or x==y or x!=z)


# not operator
#not operator takes single operand
# convert true to false   and  false to true

x=90
y=80
z=13
print(not x>y)
print(not x==y)
print(x>y  or (x==z and x>z))
print(not(x>y)  or  not(x>z))























