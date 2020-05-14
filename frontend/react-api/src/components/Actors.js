import React from 'react';

export const Actors =({ actors }) => {
  return(
    <ul>
      {actors.map(actors => {
        return(
          <li key={actors.name}>
            <h2>{actors.name}</h2>
            <h3>{actors.age}</h3>
            <h4>{actors.gender}</h4>
          </li>
        )
      })}
    </ul>
  )
};
