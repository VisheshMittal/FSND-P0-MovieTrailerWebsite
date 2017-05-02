# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

# creating different instances of class Movie
the_dark_night = media.Movie(
    "The Dark Knight",
    "02:32:00",
    "http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v8_au.jpg",
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

pulp_fiction = media.Movie(
    "Pulp Fiction",
    "02:58:00",
    "https://images-na.ssl-images-amazon.com/images/M/"
    "MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE"
    "@._V1_UX182_CR0,0,182,268_AL_.jpg",
    "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

harry_potter = media.Movie(
    "Harry Potter and the Deathly Hallows – Part 2",
    "02:10:00",
    "https://upload.wikimedia.org/wikipedia/en/d/df/Harry_Potter"
    "_and_the_Deathly_Hallows_%E2%80%93_Part_2.jpg",
    "https://www.youtube.com/watch?v=mObK5XD8udk")

pursuit_of_happyness = media.Movie(
    "The Pursuit of Happyness",
    "02:25:00",
    "http://www.gstatic.com/tv/thumb/movieposters/162523/p162523_p_v8_ad.jpg",
    "https://www.youtube.com/watch?v=89Kq8SDyvfg")

forrest_gump = media.Movie(
    "Forrest Gump",
    "02:22:00",
    "http://t3.gstatic.com/images?q=tbn:"
    "ANd9GcQCFOcMb5_zkdZg4B4JvIGLlTQTvLdtLjiS5axJJDqP1FaI8Yyx",
    "https://www.youtube.com/watch?v=uPIEn0M8su0")

gangs_of_wasseypur = media.Movie(
    "Gangs of Wasseypur - Part 2",
    "02:20:00",
    "http://media2.intoday.in/indiatoday/images/stories/"
    "gow-2_660_081412031208.jpg",
    "https://www.youtube.com/watch?v=S3PZbL8JGYQ")

movies = [the_dark_night, pulp_fiction, harry_potter,
          pursuit_of_happyness, forrest_gump, gangs_of_wasseypur]
fresh_tomatoes.open_movies_page(movies)
