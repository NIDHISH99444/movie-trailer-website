import webbrowser
class Movie :

    """
        title: Movie Title
        storyline: Short movie description
        poster_image_url: URL address of movie poster
        trailer_youtube_url: URL to youtube movie trailer
    """
    def __init__(self, movieTitle, movieStoryLine, posterImage, youtubeTrailer):
        self.title = movieTitle
        self.storyline = movieStoryLine
        self.poster_image_url = posterImage
        self.trailer_youtube_url = youtubeTrailer


    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
