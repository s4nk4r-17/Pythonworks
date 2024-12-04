from json import load

f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\datasets\\books.json")

data=load(f)

# for book in data:

#     print(book)
#________________________________________________

# all_titles=[book.get("title")for book in data]

# print(all_titles)

#or
# for book in data:

#     print(book.get("title"))

#___________________________________________________

#bookd with pages<250

# page_filter=[book.get("title")for book in data if book.get("pages")<250]

# print(page_filter)

#or

for book in data:

    if book.get("pages")<250:

        print(book.get("title"))

#____________________________________________

# print all genres
# unique_genres=set(book["genre"]for book in data)

# for genre in unique_genres:

#     print(genre)

#or

all_genres=[book.get("genre") for book in data]

print(set(all_genres))

#________________________________________________

#genre count

genre_count={genre:all_genres.count(genre)for genre in all_genres}

print(genre_count)

#___________________________________________________

#print costly book

# highest_price=0

# for book in data:

#     if book.get("price")>highest_price:

#         highest_price=book["price"]

#         most_expensive_book=book

# print(most_expensive_book)

#or

costly_book=max(data,key=lambda d:d.get("price"))

print("costliest book is -",costly_book)

#____________________________________________

#auther with more than one book

authors=[book.get("author")for book in data]

print(authors)

auther_count={author:authors.count(author)for author in authors}

print(auther_count)

more_than_one_authors=[author for author,count in auther_count.items()if count>1]

for author in more_than_one_authors:
   
    print(author)

#another way

print([k for k,v in auther_count.items()if v>1])