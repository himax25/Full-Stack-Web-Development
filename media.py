import webbrowser   # Call for the object - webbrowser.open


class Movie():
    """Define class components regarding movies

    """

    def __init__(self, movie_title, movie_storyline, movie_release_date,
                 poster_image, trailer_youtube):
        """Initialize Movie class instance valuables.
        Note:
            Do not include the 'self' paramete in the ''Arg'' section.

        Args:
            movie_title (str): the name of the movie.
            movie_storyline (str): the summary of the movie.
            movie_release_date (str): the release date of the movie as
            Month XX, Year.
            poster_image (str): the url for the movie's poster.
            trailer_youtube (str): the url of the movie trialer from
            youtubu.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.release_date = movie_release_date
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This is a method to call the movie trial website to open.
        """
        webbrowser.open(self.trailer_youtube_url)
