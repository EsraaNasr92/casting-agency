import React , {useState} from 'react';
import { Form, Input, Button } from 'semantic-ui-react'


export const AddMovie = () => {

  const [title, setTitle] = useState("");
  const [release_date, setDate] = useState("");


  return(
    <Form>

      <Form.Field>
        <Input value={title}
        placeholder="Movie title"
        onChange={e => setTitle(e.target.value)}
        />
      </Form.Field>

      <Form.Field>
        <Input value={release_date}
        placeholder="Movie release date"
        onChange={e => setDate(e.target.value)}
        />
      </Form.Field>



    <Form.Field>
      <Button
      onClick={async() => {
        const movie = {title, release_date}
        const response = await fetch('http://127.0.0.1:5000/movies', {
            method: 'POST',
            headers:{
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(movie)

        })
        if (response.ok){
          console.log("Response OK");
        }
        else {
          console.log("Response NOT OK");
        }
      }} >Submit</Button>
    </Form.Field>


    </Form>
  )
}
export default AddMovie;
