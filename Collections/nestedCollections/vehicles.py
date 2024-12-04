

cars=[

    {
        "id":1,"name":"fronx","price":1200000,"brand":"nexa",
        "colors":["red","blue","white"],
        "transmissions":["manuel","amt","cvt"]},
    {
        "id":2,"name":"baleno","price":1100000,"brand":"nexa",
        "colors":["grey","blue","white"],
        "transmissions":["manuel","amt","cvt"]},
    {
        "id":3,"name":"3xo","price":900000,"brand":"mahindra",
        "colors":["red","white","black"],
        "transmissions":["amt","cvt"]},
    {
        "id":4,"name":"punch","price":700000,"brand":"tata",
        "colors":["red","blue","white","green"],
        "transmissions":["manuel","cvt"]},
    {
        "id":5,"name":"nexon","price":1400000,"brand":"tata",
        "colors":["red","white"],
        "transmissions":["manuel","amt","cvt"]},
    {
        "id":6,"name":"kiger","price":1000000,"brand":"renault",
        "colors":["blue","white"],
        "transmissions":["manuel","cvt","dct"]},
    {
        "id":7,"name":"taigun","price":2300000,"brand":"volkswagon",
        "colors":["red","blue","white"],
        "transmissions":["manuel","cvt","torgue"]},

]


    #print count of vehicles

print(f"total vehicle=>{len(cars)}")#7

#______________________________________

for c in cars:

    print(c.get("name"))    #fronx,baleno,3xo,punch,nexon,kiger,taigun

car_model=[c.get("name") for c in cars]

print(car_model) #['fronx', 'baleno', '3xo', 'punch', 'nexon', 'kiger', 'taigun']

#_______________________________________

    #print available colours of baleno

for c in cars:

    if c.get("name")=="baleno":

        print(c.get("colors"))  #['grey', 'blue', 'white']

baleno_colors=[c.get("colors")for c in cars if c.get("name")=="baleno"]

print(baleno_colors)  #[['grey', 'blue', 'white']]


#__________________________________________

    #print all brands

for c in cars:

    print(c.get("brand"))   #nexa,nexa,mahindra,tata,tata,renault,volkswagon

all_brands=[c.get("brand") for c in cars]

print(all_brands)#['nexa', 'nexa', 'mahindra', 'tata', 'tata', 'renault', 'volkswagon']

#to print without repeatation

print(set(all_brands))  #{'tata', 'nexa', 'mahindra', 'volkswagon', 'renault'}   

#_____________________________________________

    # print car names available in amt transmission

for c in cars:

    if "amt" in c.get("transmissions"):

        print(c.get("name"))    #fronx,baleno,3xo,nexon

amt_cars=[c.get("name")for c in cars if "amt"in c.get("transmissions")]

print(amt_cars) #['fronx', 'baleno', '3xo', 'nexon']

#_______________________________________________

    # cars available in blue color

for c in cars:

    if "blue" in c.get("colors"):

        print(c.get("name"))    #fronx,baleno,punch,kiger,taigun,

blue_cars=[c.get("name")for c in cars if "blue"in c.get("colors")]

print(blue_cars)    #['fronx', 'baleno', 'punch', 'kiger', 'taigun']

#________________________________________________

    #print all transmissions

for c in cars:

    print(f"{c.get("name")}:{c.get("transmissions")}")

tranmission_types={t for c in cars for t in c.get("transmissions")}

print(tranmission_types)    #{'dct', 'amt', 'manuel', 'cvt', 'torgue'}

#________________________________________________________

    #print all colors

for c in cars:

    for col in c:

        print(c.get("colors"))

all_colors={col for c in cars for col in c.get("colors")}

print(all_colors)   #{'green', 'red', 'black', 'blue', 'grey', 'white'}      

#_______________________________________________

    #most_popular colour

color_count={col:sum(col in c.get("colors")for c in cars) for col in all_colors}

print(color_count)

most_popular_color=max(color_count)

print(most_popular_color) #white

#_________________________________________________

    #costly_car

car_cost=[c.get("price")for c in cars ]

costly_car=max(car_cost)

print(costly_car) 

#another method

cosliest_car=max(cars,key=lambda c:c.get("price"))

print(f"The cosliest car is {cosliest_car.get('name')} with a price of {cosliest_car.get("price")}")

#_________________________________________________

    #car with minimum cost

min_cost_car=min(cars,key=lambda c:c.get("price"))

print(f"The minimum cost car is {min_cost_car.get("name")} with a price of {min_cost_car.get("price")}")

#_______________________________________________

    #sort cars wrt price

sorted_cars=sorted(cars,key=lambda c:c.get("price"))

for car in sorted_cars:
    
    print(f"{car.get("name")}- Price:{car.get("price")}")

sorted_car_name={c.get("name"):c.get("price") for c in sorted_cars}

print(sorted_car_name)  #{'punch': 700000, '3xo': 900000, 'kiger': 1000000, 'baleno': 1100000, 'fronx': 1200000, 'nexon': 1400000, 'taigun': 2300000}