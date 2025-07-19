import React from 'react'
import { useParams } from 'react-router-dom'

const User = () => {
    const {id} = useParams()
  return (
    <div>
      <h3> Welcome user id : {id}</h3>
    </div>
  )
}

export default User
