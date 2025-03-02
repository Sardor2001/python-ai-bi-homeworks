import requests
import random


def get_movie_recommendation(genre_name):
    API_KEY = "00ad6ffee123dfa63e4434674dfc5777"
    BASE_URL = "https://api.themoviedb.org/3"

    try:
        # Step 1: Get the list of genres
        genre_url = f"{BASE_URL}/genre/movie/list"
        genre_params = {"api_key": API_KEY, "language": "en-US"}
        genre_response = requests.get(genre_url, params=genre_params)
        genre_response.raise_for_status()
        genres = genre_response.json()["genres"]

        # Find the genre ID for the given genre name
        genre_id = None
        for genre in genres:
            if genre["name"].lower() == genre_name.lower():
                genre_id = genre["id"]
                break

        if genre_id is None:
            print(f"Genre '{genre_name}' not found. Please try another genre.")
            return

        # Step 2: Fetch movies from the selected genre
        discover_url = f"{BASE_URL}/discover/movie"
        discover_params = {
            "api_key": API_KEY,
            "language": "en-US",
            "with_genres": genre_id,
            "sort_by": "popularity.desc",
        }
        discover_response = requests.get(discover_url, params=discover_params)
        discover_response.raise_for_status()
        movies = discover_response.json()["results"]

        if not movies:
            print(f"No movies found for the genre '{genre_name}'.")
            return

        # Step 3: Recommend a random movie
        random_movie = random.choice(movies)
        title = random_movie.get("title")
        overview = random_movie.get("overview")

        print(f"We recommend you watch: {title}")
        print(f"Overview: {overview}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    genre_name = input("Enter a movie genre (e.g., Action, Comedy, Drama): ").strip()
    get_movie_recommendation(genre_name)
