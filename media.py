import webbrowser

class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class Movie(Video):
    # The following is the documentation for the class Movie, accessed through pre-defined class-variable __doc__
    """Defines key attributes as well as operations associated with a movie"""

    # RATINGS_VALUES is a class-variable, i.e. shared by different instances of the class Movie
    RATINGS_VALUES = ['U', 'UA', 'A', 'S']
    def __init__(self, title, duration, poster_url, trailer_url):
        Video.__init__(self, title, duration)
        # The variables accessible with self are called 'instance-variables'. Every instance of the class
        # has its own copy of these variables.
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url

    def show_trailer():
        webbrowser.open(self.trailer_url)
