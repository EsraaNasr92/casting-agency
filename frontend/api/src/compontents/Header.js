import React, { Component } from 'react';


class Header extends Component {

  navTo(uri){
    window.location.href = window.location.origin + uri;
  }

  render() {
    return (
      <div className="App-header">
        <h2 onClick={() => {this.navTo('/movies')}}>Movies</h2>
        <h2 onClick={() => {this.navTo('/actors')}}>Actors</h2>
      </div>
    );
  }
}

export default Header;
