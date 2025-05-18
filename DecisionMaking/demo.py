# Short Hand If

# One line if statement:

a=5
b=2
if a > b: print(a,"is greater than ",b)

# Short Hand If ... Else

print("a is greater") if a>b else print("b is greater")

# This technique is known as Ternary Operators, or Conditional Expressions.

c = 330
d = 330
print("A") if c > d else print("=") if c == d else print("B")

# The pass Statement

# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.