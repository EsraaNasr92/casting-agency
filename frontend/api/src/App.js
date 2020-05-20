import React, { Component } from 'react';

import './stylesheets/App.css';

import Movies from "./compontents/Movies";
import Actors from "./compontents/Actors"
import Header from "./compontents/Header";

import {
  BrowserRouter as Router,
  Route,
  Switch
} from 'react-router-dom'

class App extends Component {


  render() {
    return (
    <div className="App">
      <Header path />
      <Router>
        <Switch>
          <Route path="/movies" component={Movies} />
          <Route path="/actors" component={Actors} />
        </Switch>
      </Router>
    </div>
  );

  }












}

export default App;
