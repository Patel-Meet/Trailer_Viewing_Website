import webbrowser

# This is the movie class


class Movie():
    # this is the cunstructor of the class
    def __init__(self, title, poster_url, trailer_url):
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url
