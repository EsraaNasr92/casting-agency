import React from 'react';
import { Row, Form, Col, Button } from  'semantic-ui-react'

class EditMovie extends React.Component {
  state = {
     edited: false
   }

   onSubmit = (e) => {
     e.preventDefault();
     this.editMovie(this.state.title);
     this.setState({ title: ''});
   }

   onChange = (e) =>
   this.setState({
     [e.target.name]: e.target.value
   }
   );


   render() {
     return (
       <form onSubmit={this.onSubmit}>
         <input
           type="text"
           name="title"
           placeholder="Edit Your movie"
           value={this.state.title}
           onChange={this.onChange}
         />
         <button
           type="submit">
           Edit
         </button>
       </form>
     )
   }
}

export default EditMovie;
