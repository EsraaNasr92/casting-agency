import React, { useEffect , useState} from 'react';
import { Actors } from "./Actors";


function App(){

const [actors, setActors] = useState([]);

useEffect (() => {
  fetch("actors").then(response =>
    response.json().then(data => {
    setActors(data.actors);
    console.log(data);
    })
  );
}, []);



return(
  <div className="App">
    <Actors actors={actors} />
  </div>
);


}

export default App;
