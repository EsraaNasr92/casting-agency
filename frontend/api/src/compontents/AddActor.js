import React , {useState} from 'react';
import { Form, Input, Button } from 'semantic-ui-react'


export const AddActor = () => {

  const [name, setName] = useState("");
  const [age, setAge] = useState("");
  const [gender, setGender] = useState("");


  return(
    <Form>

      <Form.Field>
        <Input value={name}
        placeholder="Actor name"
        onChange={e => setName(e.target.value)}
        />
      </Form.Field>

      <Form.Field>
        <Input value={age}
        placeholder="Actor age"
        onChange={e => setAge(e.target.value)}
        />
      </Form.Field>

      <Form.Field>

        <select   onChange={e => setGender(e.target.value)}>
           <option value="">Choose gender</option>
           <option value="male">Male</option>
           <option value="female">female</option>
        </select>


      </Form.Field>


    <Form.Field>
      <Button
      onClick={async() => {
        const actor = {name, age, gender}
        const response = await fetch('http://127.0.0.1:5000/actors', {
            method: 'POST',
            headers:{
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(actor)

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
export default AddActor;
