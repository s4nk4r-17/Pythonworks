# Given a dictionary of items and their prices, 
# write a program to apply a 10% discount to 
# all the items using dictionary comprehension.

pro_price={'apple': 65, 'mango': 63, 'pinaple': 35}

discount_price={key:value*0.9 for key,value in pro_price.items()}

print(discount_price)