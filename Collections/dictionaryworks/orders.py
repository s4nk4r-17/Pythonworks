
orders=["tea","coffee","tea","coffee","gheeroast","porotta","tea"]

#order_summary

order_dictionary={}

for item in orders:

    if item in order_dictionary:

        order_dictionary[item]+=1

    else:

        order_dictionary[item]=1

print(order_dictionary)




        