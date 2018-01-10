import fresh_tomatoes
import media


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "December 16, 2009",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")
# Movie catalog #1. Avatar

gravity = media.Movie("Gravity",
                      "A science fiction for astronautes who are stranded in "
                      "space after the mid-orbit destruction od their space "
                      "shuttle.",
                      "October 4, 2013",
                      "https://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=OiTiKOy59o4")
# Movie catalog #2. Gravity

interstellar = media.Movie("Interstellar",
                           "A science fiction for astronauts who travel throug"
                           "h a wormhole in space.",
                           "October 26, 2014",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")
# Movie catalog #3. Interstellar

the_martian = media.Movie("The Martian",
                          "A science fiction for Mars survival story with an a"
                          "stronaut and bring back home.",
                          "September 24, 2015",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")
# Movie catalog #4. The Martian

valerian = media.Movie("Valerian",
                       "A science advanture fiction for Valerian and the city "
                       "of a thousand planets",
                       "July 21, 2017",
                       "https://upload.wikimedia.org/wikipedia/en/0/07/Valerian_and_the_City_of_a_Thousand_Planets.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=Wzdta7MXCtQ")
# Movie catalog #5. Valerian

star_wars = media.Movie("Star Wars 8",
                        "This is Episode 8 of Star Wars. This story is about "
                        "Rey with resistance force ainst Kylo Ren with his ev"
                        "il force",
                        "December 15, 2017",
                        "https://upload.wikimedia.org/wikipedia/en/7/7f/Star_Wars_The_Last_Jedi.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=Q0CbN8sfihY")
# Movie catalog #6. Star Wars

movies = [avatar, gravity, interstellar, the_martian, valerian, star_wars]

fresh_tomatoes.open_movies_page(movies)
