import webbrowser       # Imports webbrowser module


class Movies():
    def __init__(self, movie_title, poster_image, youtube_trailer):
        """  Defines special method
               called __init__ """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer

    def show_youtube_trailer(self):         # Instance Method
        webbrowser.open(self.trailer_youtube_url)
