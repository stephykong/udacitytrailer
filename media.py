import webbrowser
class Movie():
    valid_ratings= ["G","PG","PG-13","R"]
    #ratings of the movie will list

    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title=movie_title #helps identify movie title
        self.storyline=movie_storyline #helps print out each specific storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
    def show_trailer(self): #shows the trailer
        webbrowser.open(self.trailer_youtube_url)
