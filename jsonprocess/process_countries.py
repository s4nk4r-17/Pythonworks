from json import load

f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\datasets\\countries.json",encoding="utf-8")

data=load(f)

#print number of countries

print(len(data))

#_____________________________________________________

#1)print all country names

all_country_names=[country.get("name") for country in data ]

print(all_country_names)

#or

for country in data:

    print(country.get("name"))


#______________________________________________________

#2)print all regions

all_regions=[regions.get("region")for regions in data]

print(set(all_regions))

#___________________________________________________

#3) print region count

region_count={region:all_regions.count(region) for region in all_regions}

print(region_count)

#__________________________________________________

#4)maximum region

max_region_count=max(region_count,key=lambda k:region_count.get(k))

print(max_region_count,region_count.get(max_region_count))

#_____________________________________________________

#5)capital of India

country_capital=[country.get("capital") for country in data if country.get("name")=="India"]

print(country_capital)

for country in data:

    if country.get("name")=="India":

        print(country.get("capital"))

#_________________________________________________

#6)countries with most number of borders


border_count={country.get("name"):len(country.get("borders",[]))for country in data}

print(border_count)

most_border_country=max(border_count,key=lambda k:border_count.get(k))

print(most_border_country,border_count.get(most_border_country))

#or another method

# max_border=max(data,key=lambda country:len(country.get("borders",[]))).get("name")

# print(max_border)

#_________________________________________________

#7)most populated country

most_populated_country=max(data,key=lambda country:country.get("population")).get("name")

print(most_populated_country)

#___________________________________________________-

#8)Sharing borders of India

for country in data:

    if country.get("name")=="India":

        print(country.get("borders"))

alpha_three_codes=[country.get("borders")for country in data if country.get("name")=="India"][0]

for code in alpha_three_codes:

    for country in data:

        if country.get("alpha3Code")==code:

            print(country.get("name"))

#____________________________________________________

