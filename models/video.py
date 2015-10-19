"""
    this class defines the video object  
"""
class Video():

    # constructor to init class vars   
    def __init__(self, title, duration, trailer_youtube_url):
        self.title    = title
        self.duration = duration
        self.trailer_youtube_url = trailer_youtube_url
