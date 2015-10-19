"""
    this class defines the movie object and it inherited from the video class
"""
from models.video import Video
class Movie(Video):

    # constructor to init class vars   
    def __init__(self, movie_title, movie_duration, movie_trailer_youtube_url, movie_story_line, movie_post_image_url, movie_director, movie_release_date, movie_iMDB_rate):

        Video.__init__(self, movie_title, movie_duration, movie_trailer_youtube_url)
        self.movie_story_line     = movie_story_line;
        self.movie_post_image_url = movie_post_image_url;
        self.movie_director         = movie_director;
        self.movie_release_date   = movie_release_date;
        self.movie_iMDB_rate      = movie_iMDB_rate;


