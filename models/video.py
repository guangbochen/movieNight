"""
    this class defines the video object  
"""
class Video():

    # constructor to init class vars   
    def __init__(self, movie_title, movie_duration, movie_trailer_youtube_url):
        self.movie_title    = movie_title
        self.movie_duration = movie_duration
        self.movie_trailer_youtube_url = movie_trailer_youtube_url
