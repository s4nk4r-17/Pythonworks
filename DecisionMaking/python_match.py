# The Python Match Statement
# Instead of writing many if..else statements, you can use the match statement.

# The match statement selects one of many code blocks to be executed.

# example

num=3
match num:

    case 1:
        print("hai")

    case 2:
        print("hello")

    case 3:
        print("good morning")

    case 4:
        print("how are you?")

# Default Value

# Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:

# example
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")

# Combine Values

# Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:

# Example

day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")