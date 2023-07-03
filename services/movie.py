from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_ids: list[int] = None,
               actors_ids: list[int] = None) -> QuerySet[Movie]:
    if genres_ids and actors_ids:
        return Movie.objects.filter(
            genres__id__in=genres_ids
        ).filter(
            actors__id__in=actors_ids
        ).distinct()
    if genres_ids:
        return Movie.objects.filter(genres__id__in=genres_ids).distinct()
    if actors_ids:
        return Movie.objects.filter(actors__id__in=actors_ids).distinct()
    return Movie.objects


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None) -> None:
    movies = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids and actors_ids:
        movies.actors.set(actors_ids)
        movies.genres.set(genres_ids)
    if genres_ids:
        movies.genres.set(genres_ids)
    if actors_ids:
        movies.actors.set(actors_ids)