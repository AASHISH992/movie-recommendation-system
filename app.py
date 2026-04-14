import streamlit as st
import pickle
import requests
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Create a requests Session to reuse TCP connections and apply retry behavior
session = requests.Session()
# Retry configuration: up to 3 retries, exponential backoff starting at 0.5s,
# retry only on the listed status codes (e.g., rate limit or server errors)
retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[429,500,502,503,504])
# Mount an HTTPAdapter with retry policy for all HTTPS requests made with this session
session.mount('https://', HTTPAdapter(max_retries=retries))


# Load precomputed data: movie metadata and similarity matrix
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# TMDB API key used to fetch poster paths
TMDB_API_KEY = "Enter your TMDB API Key"


# Fetch movie poster URL from TMDB using the movie's TMDB ID.
# Returns full image URL or None if unavailable or on error.
def fetch_poster(movie_id):
    if not movie_id:
        return None
    try:
        # Use the session (with retries) and a timeout to avoid hanging
        r = session.get(
            f'https://api.themoviedb.org/3/movie/{movie_id}',
            params={'api_key': TMDB_API_KEY, 'language': 'en-US'},
            timeout=5
        )
        r.raise_for_status()
        data = r.json()
        path = data.get('poster_path')
        if path:
            return "https://image.tmdb.org/t/p/w500" + path
    except Exception:
        # Silently ignore network/response issues and return None
        pass
    return None  # No poster available


# Recommend top-5 similar movies (excluding the selected one).
# Returns two lists: movie names and corresponding poster URLs (or None).
def recommend(movie):
    # Find the index of the selected movie in the DataFrame
    index = movies[movies['title'] == movie].index[0]
    # Get similarity scores and sort in descending order
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    movie_names = []
    movie_posters = []
    # Take next 5 most similar movies (skip the first which is the movie itself)
    for i in distances[1:6]:
        movie_row = movies.iloc[i[0]]
        # Adapt to your DataFrame column name for TMDB ID (here assumed 'id')
        movie_id = movie_row.get('id')
        # Fetch poster URL (may return None)
        movie_posters.append(fetch_poster(movie_id) if movie_id is not None else None)
        movie_names.append(movie_row.title)

    return movie_names, movie_posters


# Streamlit UI
st.header('Movie Recommender System')

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Recommend'):
    result = recommend(selected_movie)
    # recommend() returns tuple of lists; if you change it to return a string on error, handle it here
    if isinstance(result, str):
        st.write(result)
    else:
        movie_names, movie_posters = result
        cols = st.columns(5)
        # Display name + poster (or placeholder text) in 5 columns
        for i, col in enumerate(cols):
            with col:
                st.text(movie_names[i])
                if movie_posters[i]:
                    st.image(movie_posters[i])
                else:
                    st.write("No poster available")
