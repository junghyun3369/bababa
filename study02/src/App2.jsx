import {useState, useEffect} from 'react';

const Test1 = () => {
  const [cnt, setCnt] = useState(0)
  return (
    <p>호출 횟수 : {cnt}</p>
  )
}

const App2 = () => (<Test1 />)

export default App2