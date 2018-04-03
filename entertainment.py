import media
import fresh_tomatoes

"""Creating Instance of Movie Class"""
toy_story= media.Movie("toyStory",
                     "A story of a body and his toys that come to life",
                     "http://www.cultjer.com/img/ug_photo/2015_09/32772420150915154419.jpg",
                     "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

matrix = media.Movie("Matrix",
                     "A movie about the reality of life itself.",
                     "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")


whiplash = media.Movie("Whiplash",
                       "A promising young drummer enrolls at a cut-throat music conservatory where his dreams of greatness are mentored by an instructor who will stop at nothing to realize a student's potential.",
                       "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSyLORvKKvCi7-vy8vwi2s8F62aG7D36H15A8rOVfP2d7koyA9I",
                       "https://www.youtube.com/watch?v=tYkuvB2f5XU")

mad_max_fury_road = media.Movie("Mad Max Fury Road",
                                "In a stark desert landscape where humanity is broken, two rebels just might be able to restore order: Max, a man of action and of few words, and Furiosa, a woman of action who is looking to make it back to her childhood homeland.",
                                "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSY9szIPbtk1-hwxdEVRJIHT_pgYGNnFkFSWsCjlKFGP3Pu77Oo",
                                "https://www.youtube.com/watch?v=YWNWi-ZWL3c")

above_the_rim = media.Movie("Above the Rim",
                            "A promising New York City high school basketball star and his relationships with two people.",
                            "http://upload.wikimedia.org/wikipedia/en/b/b6/Above_the_rim_poster.jpg",
                            "https://www.youtube.com/watch?v=sEsCXWD7-Cc")

"""Adding Instance to the List"""
movies=[toy_story, avatar, matrix, whiplash, mad_max_fury_road, above_the_rim]
"""Calling open_movies_page function inside fresh_tomatoes that displays movie  in the list on web page """
fresh_tomatoes.open_movies_page(movies)
