import React, { Component } from 'react';
import logo from '../logo.svg';
import '../stylesheets/Header.css';

class Header extends Component {

  navTo(uri){
    window.location.href = window.location.origin + uri;
  }

  render() {
    return (
      <div className="App-header">
        <h2 onClick={() => {this.navTo('/movie')}}>Movie</h2>
        <h2 onClick={() => {this.navTo('/actor')}}>actor</h2>
      </div>
    );
  }
}

export default Header;
