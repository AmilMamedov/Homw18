from dao.model.movie import Movie
from dao.model.director import Director
from dao.model.genre import Genre

data_for_db = [
    Movie(id=1, title='The Shawshank Redemption',
          description='Over the course of several years, two convicts form a friendship, '
                      'seeking consolation and, eventually, redemption through basic compassion.',
          trailer='https://www.youtube.com/watch?v=NmzuHjWmXOc', year=1994, rating=9.3,
          genre_id=1, director_id=1
          ),
    Movie(id=2, title='The Godfather',
          description='The aging patriarch of an organized crime dynasty in postwar New York City '
                      'transfers control of his clandestine empire to his reluctant youngest son.',
          trailer='https://www.youtube.com/watch?v=UaVTIH8mujA', year=1972, rating=9.2,
          genre_id=1, director_id=2
          ),
    Movie(id=3, title='The Dark Knight',
          description='When the menace known as the Joker wreaks havoc and chaos on the people of '
                      'Gotham, Batman must accept one of the greatest psychological and physical tests '
                      'of his ability to fight injustice.',
          trailer='https://www.youtube.com/watch?v=EXeTwQWrcwY', year=2008, rating=9.0,
          genre_id=2, director_id=3
          ),
    Movie(id=4, title="Schindler's List",
          description='In German-occupied Poland during World War II, industrialist Oskar Schindler '
                      'gradually becomes concerned for his Jewish workforce after witnessing their '
                      'persecution by the Nazis.',
          trailer='https://www.youtube.com/watch?v=EXeTwQWrcwY', year=1993, rating=9.0,
          genre_id=1, director_id=4
          ),
    Movie(id=5, title="Interstellar",
          description="A team of explorers travel through a wormhole in space in an attempt to ensure "
                      "humanity's survival.",
          trailer='https://www.youtube.com/watch?v=zSWdZVtXT7E', year=2014, rating=8.6,
          genre_id=1, director_id=3
          ),
    Movie(id=6, title="The Terminal",
          description="An Eastern European tourist unexpectedly finds himself stranded in JFK airport, and "
                      "must take up temporary residence there.",
          trailer='https://www.youtube.com/watch?v=iZqQRmhRvyg', year=2004, rating=7.4,
          genre_id=3, director_id=4
          ),
    Director(id=1, name='Frank Darabont'),
    Director(id=2, name='Francis Ford Coppola'),
    Director(id=3, name='Christopher Nolan'),
    Director(id=4, name='Steven Spielberg'),
    Genre(id=1, name='Drama'),
    Genre(id=2, name='Action'),
    Genre(id=3, name='Comedy')
]
