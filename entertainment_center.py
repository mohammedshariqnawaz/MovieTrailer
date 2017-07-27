import fresh_tomatoes       # Imports fresh_tomatoes file
import media        # Imports the media file

""" Class Instances are being
    created for each of the movies """

toy_story = media.Movies("Toy Story",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")  # NOQA

shawshank_redemption = media.Movies("Shawshank Redemption",
                                "https://www.movieposter.com/posters/archive/main/42/MPW-21321",  # NOQA
                                "https://www.youtube.com/watch?v=NmzuHjWmXOc")  # NOQA

the_godfather = media.Movies("The Godfather",
                     "http://thumbs3.ebaystatic.com/d/l225/m/mvJN4K4VOmRUhIBD7SbuE2w.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=5DO-nDW43Ik")  # NOQA

the_dark_knight = media.Movies("The Dark Knight",
                               "http://host.trivialbeing.org/up/tdk-jul1-dark-knight-poster-stupidbats.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=EXeTwQWrcwY")  # NOQA

inception = media.Movies("Inception",
          "http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-5.jpg",  # NOQA
          "https://www.youtube.com/watch?v=YoHD9XEInc0")  # NOQA

jurassic_park = media.Movies("Jurassic Park",
              "https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg",  # NOQA
              "https://www.youtube.com/watch?v=lc0UehYemQA")  # NOQA


movies = [toy_story, shawshank_redemption,
          the_godfather, inception,
          the_dark_knight, jurassic_park]  # List of the movies in an array
fresh_tomatoes.open_movies_page(movies)
