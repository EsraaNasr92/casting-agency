import React, { Component } from 'react';
import AddActor from './AddActor';
import EditActor from './EditActor';
import '../stylesheets/App.css';




class Actors extends Component {

  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      actors: []
    };
  }

  componentDidMount() {
      fetch("http://127.0.0.1:5000/actors")
        .then(res => res.json())
        .then(
          (result) => {
            this.setState({
              isLoaded: true,
              actors: result.actors
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


deleteMovie(actor_id){
  if(window.confirm('Are you sure?')){
    fetch('http://127.0.0.1:5000/actors/' + actor_id, {
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
        const { error, isLoaded, actors } = this.state;
        if (error) {
          return <div>Error: {error.message}</div>;
        } else if (!isLoaded) {
          return <div>Loading...</div>;
        } else {
          return (

            <div className="container">
                <div className="col-xs-8">
                <h1>Actors List</h1>
                <AddActor />
                {actors.map(actors => (
                  <div className="card">
                   <div className="card-body">
                      <div onClcik={this.changeEditMode}>
                        <h5 className="card-title">Actor name: {actors.name} </h5>
                        </div>
                      <h6 className="card-subtitle mb-2 text-muted">
                        Actor age: {actors.age}
                      </h6>
                      <p>Gender: {actors.gender}</p>
                      <button className="btn btn-danger"  onClick={() => this.deleteMovie(actors.id)}>Delete</button>
                      <button className="edit-btn" onClick={() => this.editMovie(actors.id)}>EDIT</button>


                    </div>

                  </div>
                  ))}
                </div>
             </div>
          );


        }
      }









}

export default Actors;
