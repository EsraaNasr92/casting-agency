
    import React from 'react'

    const MovieView = ({ movies }) => {
      return (
        <div>
          <center><h1>Contact List</h1></center>
          {movies.map((movie) => (
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">{movie.title}</h5>

              </div>
            </div>
          ))}
        </div>
      )
    };

    export default MovieView
