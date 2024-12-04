# user_input=input("enter bracker pairs:")# ([])

# valid=True

# stack=[]

# bracket_pairs={"(":")","{":"}","[":"]","<":">"}

# for symbol in user_input: #(

#     if symbol in bracket_pairs:

#         stack.append(symbol)  #stack=['(','[']

#     elif symbol in bracket_pairs.values():

#         if not stack or bracket_pairs[stack.pop()] != symbol: 
            
#             valid=False

#             break

# print(stack)

# if valid and not stack:

#     print("Valid")

# else:

#     print("Not valid")


#_______________________________________________________________________


user_input=input("enter bracker pairs:") # ([])

bracket_pairs={
    "(":")",
    "{":"}",
    "[":"]",
    "<":">"
    
}

symbol_stack=[]

top=-1

is_valid=True

for symbol in user_input:

    if symbol in bracket_pairs:

        top=top+1

        symbol_stack.append(symbol) # Push onto the stack   

    elif top>=0 and symbol==bracket_pairs.get(symbol_stack[top]):# If it's a matching closing bracket

        top=top-1

        symbol_stack.pop() # Pop the last opening bracket

    else:

        is_valid=False
        break
    
if len(symbol_stack)==0 and is_valid:

    print("valid")

else:

    print("Not Valid")
