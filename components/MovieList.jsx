import React, { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

const MovieList = () => {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/movies")
      .then(res => setMovies(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      {movies.map(movie => (
        <div key={movie.id}>
          <Link to={`/movie/${movie.id}`}>
            <h3>{movie.title}</h3>
            <img src={`https://image.tmdb.org/t/p/w500${movie.poster_url}`} alt={movie.title} />
          </Link>
        </div>
      ))}
    </div>
  );
};

export default MovieList;
