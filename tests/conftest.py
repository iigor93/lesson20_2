import pytest
from dao.director import DirectorDAO
from dao.model.director import Director
from dao.genre import GenreDAO
from dao.model.genre import Genre
from dao.movie import MovieDAO
from dao.model.movie import Movie
from unittest.mock import MagicMock


@pytest.fixture()
def director_dao():
    """фикстура для класса DirectorDao"""
    director_dao = DirectorDAO(None)

    quentin = Director(id=1, name='Quentin Tarantino')
    gay = Director(id=2, name='Gay Richie')
    george = Director(id=3, name='George Lukas')

    director_dao.get_one = MagicMock(return_value=quentin)
    director_dao.get_all = MagicMock(return_value=[quentin, gay, george])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.update = MagicMock()
    director_dao.partially_update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


@pytest.fixture()
def genre_dao():
    """фикстура для класса GenreDao"""
    genre_dao = GenreDAO(None)

    comedy = Genre(id=1, name='Comedy')
    thriller = Genre(id=2, name='Thriller')
    tv_show = Genre(id=3, name='TV-Show')

    genre_dao.get_one = MagicMock(return_value=comedy)
    genre_dao.get_all = MagicMock(return_value=[comedy, thriller, tv_show])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.update = MagicMock()
    genre_dao.partially_update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao


@pytest.fixture()
def movie_dao():
    """фикстура для класса MovieDao"""
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title='Movie_1', description='Movie_1', trailer='Movie_1',
                    year=2020, rating=7.8, genre_id=2, director_id=4)
    movie_2 = Movie(id=1, title='Movie_2', description='Movie_2', trailer='Movie_2',
                    year=2020, rating=7.8, genre_id=2, director_id=4)
    movie_3 = Movie(id=1, title='Movie_3', description='Movie_3', trailer='Movie_3',
                    year=2020, rating=7.8, genre_id=2, director_id=4)

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.update = MagicMock()
    movie_dao.partially_update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao
