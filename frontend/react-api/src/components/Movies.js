import React from 'react';

export const Movies =({ movies }) => {
  return(
    <ul>
      {movies.map(movies => {
        return(
          <li key={movies.title}>
            <h2>{movies.title}</h2>
            <h4>{movies.release_date}</h4>
          </li>
        )
      })}
    </ul>
  )
};
