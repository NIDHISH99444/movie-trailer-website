import webbrowser
class Movie :

    """ This class provides a way to store movie related information
    Attributes:
        title: The title of the movie
        storyline: A short description of what the movie is about
        poster_image_url: The URL address of a poster of the movie
        trailer_youtube_url: A link to a YouTube.com page that shows the trailer of the movie
    """
    def __init__(self, movieTitle, movieStoryLine, posterImage, youtubeTrailer):
        self.title = movieTitle
        self.storyline = movieStoryLine
        self.poster_image_url = posterImage
        self.trailer_youtube_url = youtubeTrailer
        print("Done my job......")

    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
