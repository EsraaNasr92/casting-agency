import React, { Component } from 'react';



class Header extends Component {

  navTo(uri){
    window.location.href = window.location.origin + uri;
  }

  render() {
    return (
      <div className="App-header">
        <h2 onClick={() => {this.navTo('/AddMovie')}}>Movie</h2>
      </div>
    );
  }
}

export default Header;
