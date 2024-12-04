#Movie
#title,rating,run_time,director,genre

class Movie:

    title:str

    rating:int

    run_time:int

    director:str

    genre:str

    # Constructor to initialize the attributes
    def __init__(self,title,rating,run_time,director,genre):

        self.title=title
        self.rating=rating
        self.run_time=run_time
        self.director=director
        self.genre=genre

    # Method to display movie details
    def display_movie(self):

        print(self.title,self.rating,self.run_time,self.director,self.genre)
        
# Creating an instance of the Movie class
movie1=Movie("Arm",7.8,170,"Jithin Laal","Drama")

movie2=Movie("KGF",7.5,180,"Prashan Neel","Action")

# Displaying movie details
movie1.display_movie()
movie2.display_movie()