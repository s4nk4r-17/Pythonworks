

#key:valye pairs

# dictionary

#creating an employee dictionary with id=100,name=vipin,department=hr,salary=25000

employee={"id":100,"name":"vipin","department":"hr","salary":25000}

print(employee["id"])


#___________________________________________________

#create a dictionary product with keys: id,title,price,brand

product={"id":102301,"title":"s24","price":89000,"brand":"samsung"}

print(product)

print(product["id"])

#update product price as 990000

product["price"]=99000

print(product)

product["warranty"]="5years"

print(product)

product["offer"]=79000

print(product)

if("offer" in product):
    
    product["offer"]=10

else:

    product["offer"]=20

print(product)
