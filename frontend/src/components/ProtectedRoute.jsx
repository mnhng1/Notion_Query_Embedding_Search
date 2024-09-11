import { Navigate, Outlet } from 'react-router-dom'

const PrivateRoutes = () => {
  let auth = {'token':true}
return (
    auth.token ? <Outlet/> : <Navigate to='http://localhost:8000/oauth/login'/>
  )
}


export default PrivateRoutes