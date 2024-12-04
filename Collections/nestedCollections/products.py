products=[
    {"id":1,"title":"s23ultra","brand":"samsung","price":78000},
    {"id":2,"title":"a17","brand":"samsung","price":18000},
    {"id":3,"title":"m50","brand":"samsung","price":16000},
    {"id":4,"title":"pocom3","brand":"poco","price":15000},
    {"id":7,"title":"vivov50","brand":"vivo","price":25000},
    {"id":5,"title":"oppof19pro","brand":"oppo","price":27000},
    {"id":6,"title":"iphone16pro","brand":"apple","price":150000},
    {"id":8,"title":"nokia105","brand":"nokia","price":900}

]

# total number of mobiles


print(len(products))#8

# print mobile titles

for m in products:

    print(m.get("title"))#s23ultra,a17,m50,pocom3,vivov50,oppof19pro,iphone16pro,nokia105

mobile_titles=[m.get("title")for m in products]

print(mobile_titles)#['s23ultra', 'a17', 'm50', 'pocom3', 'vivov50', 'oppof19pro', 'iphone16pro', 'nokia105']

# print samsung mobiles

for m in products:

    if m.get("brand")=="samsung":

        print(m.get("title"))#s23ultra,a17,m50

samsung_mobiles=[m.get("title")for m in products if m.get("brand")=="samsung"]

print(samsung_mobiles)#['s23ultra', 'a17', 'm50']

#_____________________________________________




print(max(products,key=lambda d:d.get("price")))#{'id': 6, 'title': 'iphone16pro', 'brand': 'apple', 'price': 150000}

costly_mobile=max(products,key=lambda d:d.get("price"))

max_price=costly_mobile.get("price")

costly_mobile=[m.get("title") for m in products if m.get("price")==max_price]

print(max_price)

#______________________________________________

#print samsung mobile count

samsung_count=[product for product in products if product["brand"]=="samsung" ]

print(len(samsung_count))#3

#__________________________________________

all_brands=[p.get("brand")for p in products]

print(all_brands)#['samsung', 'samsung', 'samsung', 'poco', 'vivo', 'oppo', 'apple', 'nokia']

brand_count={b:all_brands.count(b)for b in all_brands}

print(brand_count)#{'samsung': 3, 'poco': 1, 'vivo': 1, 'oppo': 1, 'apple': 1, 'nokia': 1}