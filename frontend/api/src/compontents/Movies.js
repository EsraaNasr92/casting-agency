import React, { Component } from 'react';
import AddMovie from './AddMovie';
import EditMovie from './EditMovie';
import '../stylesheets/App.css';




class Movies extends Component {

  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      movies: []
    };
  }

  componentDidMount() {
      fetch("http://127.0.0.1:5000/movies")
        .then(res => res.json())
        .then(
          (result) => {
            this.setState({
              isLoaded: true,
              movies: result.movies
            });
          },
          (error) => {
            this.setState({
              isLoaded: true,
              error
            });
          }
        )
    }


deleteMovie(movie_id){
  if(window.confirm('Are you sure?')){
    fetch('http://127.0.0.1:5000/movies/' + movie_id, {
      method: 'DELETE',
      header:{
        'Accept': 'application/json',
        'Content-type': 'application/json'
      }
    })
  }
}


changeEditMode = () => {
  console.log("Should go to edit mode now");
}


    render() {
        const { error, isLoaded, movies } = this.state;
        if (error) {
          return <div>Error: {error.message}</div>;
        } else if (!isLoaded) {
          return <div>Loading...</div>;
        } else {
          return (

            <div className="container">
                <div className="col-xs-8">
                <h1>Movies List</h1>
                <AddMovie />
                {movies.map(movies => (
                  <div className="card">
                   <div className="card-body">
                      <div onClcik={this.changeEditMode}>
                        <h5 className="card-title">Movie title: {movies.title} </h5>
                        </div>
                      <h6 className="card-subtitle mb-2 text-muted">
                        Release date: {movies.release_date}
                      </h6>
                      <button className="btn btn-danger"  onClick={() => this.deleteMovie(movies.id)}>Delete</button>
                      <button className="edit-btn" onClick={() => this.editMovie(movies.id)}>EDIT</button>


                    </div>

                  </div>
                  ))}
                </div>
             </div>
          );


        }
      }









}

export default Movies;
