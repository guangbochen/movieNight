from models.movie import Movie
class MoviesController():

    def __init__(self):
        self.movie_list = []
        self.add_favorite_movies()

    def add_favorite_movies(self):
        first_movie = Movie('The Legend of 1900', '165 min', 'https://www.youtube.com/embed/2uf-LDlZMFE', 'A baby boy, discovered in 1900 on an ocean liner, grows into a musical prodigy, never setting foot on land.', 'http://ia.media-imdb.com/images/M/MV5BMTA3MTcxNjE0NzNeQTJeQWpwZ15BbWU4MDc3NjUxNDAx._V1_SX214_AL_.jpg', 'Giuseppe Tornatore', '1998', '8.1')

        second_movie = Movie('Black Hawk Down', '144 min', 'https://www.youtube.com/embed/qe9xbgtige0', '123 elite U.S. soldiers drop into Somalia to capture two top lieutenants of a renegade warlord and find themselves in a desperate battle with a large force of heavily-armed Somalis.', 'http://ia.media-imdb.com/images/M/MV5BMTQxODgzMjYyN15BMl5BanBnXkFtZTgwNDU4NTYxMTE@._V1_SY317_CR0,0,214,317_AL_.jpg', 'Ridley Scott', '2001', '7.7')

        third_movie = Movie('The Kite Runner', '128 min', 'https://www.youtube.com/embed/sLtavGjAOJY', 'After spending years in California, Amir returns to his homeland in Afghanistan to help his old friend Hassan, whose son is in trouble.', 'http://ia.media-imdb.com/images/M/MV5BODcyNjY2MjEwM15BMl5BanBnXkFtZTcwODQ0MzI1MQ@@._V1_SY317_CR6,0,214,317_AL_.jpg', 'Marc Forster', '2007', '7.6')

        fourth_movie = Movie('The Shawshank Redemption', '142 min', 'https://www.youtube.com/embed/6hB3S9bIaco', 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.', 'http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX214_AL_.jpg', 'Frank Darabont', '1994', '9.3')

        fifth_movie = Movie('The Wolf of Wall Street', '180 min', 'https://www.youtube.com/embed/iszwuX1AK6A', 'Based on the true story of Jordan Belfort, from his rise to a wealthy stock-broker living the high life to his fall involving crime, corruption and the federal government.', 'http://ia.media-imdb.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_SX214_AL_.jpg', 'Martin Scorsese', '2013', '8.2')

        sixth_movie = Movie('Inception', '148 min', 'https://www.youtube.com/embed/YoHD9XEInc0', 'A thief who steals corporate secrets through use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.', 'http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX214_AL_.jpg', 'Christopher Nolan', '2010', '8.8')

        self.movie_list.append(first_movie)
        self.movie_list.append(second_movie)
        self.movie_list.append(third_movie)
        self.movie_list.append(fourth_movie)
        self.movie_list.append(fifth_movie)
        self.movie_list.append(sixth_movie)

        return self.movie_list

    def get_favorite_movies(self):
        return self.movie_list


