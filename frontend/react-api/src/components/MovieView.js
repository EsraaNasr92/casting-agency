import React, { useEffect , useState} from 'react';
import { Movies } from "./Movies";


function App(){

const [movies, setMovies] = useState([]);

useEffect (() => {
  fetch("movies").then(response =>
    response.json().then(data => {
    setMovies(data.movies);
    console.log(data);
    })
  );
}, []);



return(
  <div className="App">
    <Movies movies={movies} />
  </div>
);


}

export default App;
