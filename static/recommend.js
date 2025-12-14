/**
 * @file This file contains the client-side logic for the movie recommendation page.
 * @author Chirag127
 */

/**
 * The API key for The Movie Database (TMDB).
 * @type {string}
 */
const TMDB_API_KEY = 'e683fb6c23f18c82dbbb800d49ea8702';

/**
 * The base URL for the TMDB API.
 * @type {string}
 */
const TMDB_BASE_URL = 'https://api.themoviedb.org/3';

/**
 * Handles the input event for the movie search bar.
 * @param {Event} e The input event.
 */
const handleMovieInput = (e) => {
  const movieButton = document.querySelector('.movie-button');
  movieButton.disabled = e.target.value === '';
};

/**
 * Fetches movie details from the TMDB API.
 * @param {string} title The title of the movie to search for.
 * @returns {Promise<object>} A promise that resolves to the movie details.
 */
const fetchMovieDetails = async (title) => {
  const response = await fetch(`${TMDB_BASE_URL}/search/movie?api_key=${TMDB_API_KEY}&query=${title}`);
  if (!response.ok) {
    throw new Error('Invalid Request');
  }
  const movie = await response.json();
  if (movie.results.length < 1) {
    throw new Error('Movie not found');
  }
  return movie.results[0];
};

/**
 * Fetches movie recommendations from the server.
 * @param {string} title The title of the movie to get recommendations for.
 * @returns {Promise<string[]>} A promise that resolves to an array of recommended movie titles.
 */
const fetchMovieRecommendations = async (title) => {
  const response = await fetch('/similarity', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: `name=${encodeURIComponent(title)}`,
  });
  if (!response.ok) {
    throw new Error('Error fetching recommendations');
  }
  const recs = await response.text();
  if (recs === 'Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies') {
    throw new Error(recs);
  }
  return recs.split('---');
};

/**
 * Fetches additional movie details from the TMDB API.
 * @param {number} movieId The ID of the movie.
 * @returns {Promise<object>} A promise that resolves to the movie details.
 */
const fetchAdditionalMovieDetails = async (movieId) => {
  const response = await fetch(`${TMDB_BASE_URL}/movie/${movieId}?api_key=${TMDB_API_KEY}`);
  if (!response.ok) {
    throw new Error('API Error!');
  }
  return response.json();
};

/**
 * Fetches movie posters for the recommended movies.
 * @param {string[]} movies The list of recommended movie titles.
 * @returns {Promise<string[]>} A promise that resolves to an array of movie poster URLs.
 */
const fetchMoviePosters = async (movies) => {
  const posterPromises = movies.map(async (movie) => {
    const response = await fetch(`${TMDB_BASE_URL}/search/movie?api_key=${TMDB_API_KEY}&query=${movie}`);
    if (!response.ok) {
      return '';
    }
    const data = await response.json();
    return `https://image.tmdb.org/t/p/original${data.results[0].poster_path}`;
  });
  return Promise.all(posterPromises);
};

/**
 * Fetches the cast for a movie.
 * @param {number} movieId The ID of the movie.
 * @returns {Promise<object>} A promise that resolves to an object containing cast information.
 */
const fetchMovieCast = async (movieId) => {
  const response = await fetch(`${TMDB_BASE_URL}/movie/${movieId}/credits?api_key=${TMDB_API_KEY}`);
  if (!response.ok) {
    throw new Error('Invalid Request!');
  }
  const credits = await response.json();
  const topCast = credits.cast.slice(0, 10);
  return {
    cast_ids: topCast.map((cast) => cast.id),
    cast_names: topCast.map((cast) => cast.name),
    cast_chars: topCast.map((cast) => cast.character),
    cast_profiles: topCast.map((cast) => `https://image.tmdb.org/t/p/original${cast.profile_path}`),
  };
};

/**
 * Fetches details for each cast member.
 * @param {number[]} castIds The list of cast member IDs.
 * @returns {Promise<object>} A promise that resolves to an object containing cast details.
 */
const fetchIndividualCastDetails = async (castIds) => {
  const castDetailsPromises = castIds.map(async (castId) => {
    const response = await fetch(`${TMDB_BASE_URL}/person/${castId}?api_key=${TMDB_API_KEY}`);
    if (!response.ok) {
      return {};
    }
    const castDetails = await response.json();
    return {
      birthday: new Date(castDetails.birthday).toDateString().split(' ').slice(1).join(' '),
      biography: castDetails.biography,
      place_of_birth: castDetails.place_of_birth,
    };
  });
  const castDetails = await Promise.all(castDetailsPromises);
  return {
    cast_bdays: castDetails.map((detail) => detail.birthday),
    cast_bios: castDetails.map((detail) => detail.biography),
    cast_places: castDetails.map((detail) => detail.place_of_birth),
  };
};

/**
 * Renders the movie details and recommendations on the page.
 * @param {object} movieDetails The details of the movie.
 * @param {string[]} recommendedMovies The list of recommended movie titles.
 * @param {string} movieTitle The title of the movie.
 */
const renderMovieDetails = async (movieDetails, recommendedMovies, movieTitle) => {
  const {
    imdb_id,
    poster_path,
    overview,
    genres,
    vote_average,
    vote_count,
    release_date,
    runtime,
    status,
  } = await fetchAdditionalMovieDetails(movieDetails.id);

  const genre_list = genres.map((genre) => genre.name).join(', ');
  const finalRuntime = runtime % 60 === 0
    ? `${Math.floor(runtime / 60)} hour(s)`
    : `${Math.floor(runtime / 60)} hour(s) ${runtime % 60} min(s)`;

  const posters = await fetchMoviePosters(recommendedMovies);
  const cast = await fetchMovieCast(movieDetails.id);
  const individualCast = await fetchIndividualCastDetails(cast.cast_ids);

  const details = {
    title: movieTitle,
    cast_ids: JSON.stringify(cast.cast_ids),
    cast_names: JSON.stringify(cast.cast_names),
    cast_chars: JSON.stringify(cast.cast_chars),
    cast_profiles: JSON.stringify(cast.cast_profiles),
    cast_bdays: JSON.stringify(individualCast.cast_bdays),
    cast_bios: JSON.stringify(individualCast.cast_bios),
    cast_places: JSON.stringify(individualCast.cast_places),
    imdb_id,
    poster: `https://image.tmdb.org/t/p/original${poster_path}`,
    genres: genre_list,
    overview,
    rating: vote_average,
    vote_count: vote_count.toLocaleString(),
    release_date: new Date(release_date).toDateString().split(' ').slice(1).join(' '),
    runtime: finalRuntime,
    status,
    rec_movies: JSON.stringify(recommendedMovies),
    rec_posters: JSON.stringify(posters),
  };

  const response = await fetch('/recommend', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams(details),
  });
  const html = await response.text();
  document.querySelector('.results').innerHTML = html;
  document.getElementById('autoComplete').value = '';
  window.scrollTo(0, 0);
};

/**
 * Handles the click event for the movie search button.
 */
const handleMovieButtonClick = async () => {
  const title = document.querySelector('.movie').value;
  if (title === '') {
    document.querySelector('.results').style.display = 'none';
    document.querySelector('.fail').style.display = 'block';
    return;
  }
  document.getElementById('loader').style.display = 'block';
  try {
    const movieDetails = await fetchMovieDetails(title);
    const recommendedMovies = await fetchMovieRecommendations(movieDetails.original_title);
    await renderMovieDetails(movieDetails, recommendedMovies, movieDetails.original_title);
  } catch (error) {
    document.querySelector('.fail').style.display = 'block';
    document.querySelector('.results').style.display = 'none';
  } finally {
    document.getElementById('loader').style.display = 'none';
  }
};

/**
 * Handles the click event for the recommended movie cards.
 * @param {HTMLElement} e The clicked element.
 */
const handleRecommendCardClick = (e) => {
  const title = e.getAttribute('title');
  handleMovieButtonClick(title);
};

document.addEventListener('DOMContentLoaded', () => {
  const source = document.getElementById('autoComplete');
  source.addEventListener('input', handleMovieInput);
  document.querySelector('.movie-button').addEventListener('click', handleMovieButtonClick);
});
