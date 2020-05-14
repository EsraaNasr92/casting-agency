import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Switch
} from 'react-router-dom'

// import logo from './logo.svg';
import './stylesheets/App.css';
import MovieView from './components/MovieView';
import Header from './components/Header';
import ActorView from './components/ActorView';


class App extends Component {
  render() {
    return (
    <div className="App">
      <Header path />
      <Router>
        <Switch>

          <Route path="/movie" component={MovieView} />
          <Route path="/actor" component={ActorView} />

        </Switch>
      </Router>
    </div>
  );

  }
}
/* class App extends Component {



  state = {movies: []}

        componentDidMount() {
        fetch('/movies')
        .then(response => response.json())
        .then((data) => {
          this.setState({ data: data.movies })
        })
        .catch(console.log)
      }

      render() {
        return (
          <MovieView movies={this.state.movies} />
        )
      }



} */

/* function App(){

useEffect (() => {
  fetch("movies").then(response =>
    response.json().then(data => {
      console.log(data);
    })
  );
}, []);


return(<div className="App"></div>);


} */

export default App;
