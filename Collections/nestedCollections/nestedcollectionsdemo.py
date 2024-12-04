
box=[
    {"color":"blue","size":7},
    {"color":"red","size":5},
    {"color":"yellow","size":6},
    {"color":"green","size":9},
    {"color":"green","size":4},
    {"color":"red","size":6}

]

for b in box:

    print(b.get("color"))

color=[b.get('color')for b in box ]

print(color)




#_____________________________________________

movies=[
    {"id":1,"title":"kgf","year":2018,"language":"kannada","run_time":150},
    {"id":2,"title":"kgf2","year":2023,"language":"kannada","run_time":160},
    {"id":3,"title":"goat life","year":2024,"language":"malayalam","run_time":120},
    {"id":4,"title":"avesham","year":2024,"language":"malayalam","run_time":130},
    {"id":5,"title":"vazha","year":2024,"language":"malayalam","run_time":140},
    {"id":6,"title":"arm","year":2024,"language":"malayalam","run_time":150},
    {"id":7,"title":"goat","year":2024,"language":"tamil","run_time":160},

]

#highest_runtime_movie


highest_runtime_movie=max(movies,key=lambda d:d.get("run_time"))

print(highest_runtime_movie.get("title"))

#malayalam movies count

malayalam_movies=[m for m in movies if m.get("language")=="malayalam" ]

print(len(malayalam_movies))


# print years

all_years=[m.get("year")for m in movies]

year_count={y:all_years.count(y)for y in all_years}

print(all_years)

print(year_count)
