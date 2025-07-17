import { useState } from 'react'
import './App.css'

const Test1 = () => {
  const [a, setA] = useState(0)
  const btn = () => setA(a + 1)
  return (
    <>
      <button type='button' onClick={btn}>변경</button>
      <h1>{a}</h1>
    </>
  )
}

const Test2 = () => {
  const [txt, setTxt] = useState("")
  const submitEvent = (e) => {
    e.preventDefault();
    setTxt(e.target.txt.value)
  }
  return (
    <form onSubmit={submitEvent}>
      <input type='text' name='txt' />
      <button type='submit'>전송</button>
      <h1>{txt}</h1>
    </form>
  )
}

const Test3 = () => {
  const [list, setList] = useState([])
  const [txt, setTxt] = useState("")
  const submitEvent = (e) => {
    e.preventDefault();
    setList([txt, ...list])
  }
  const changeEvent = (e) => {
    setTxt(e.target.value)
  }
  return (
    <form onSubmit={submitEvent}>
      <input type='text' name='txt' onChange={changeEvent} />
      <button type='submit'>전송</button>
      {
        list.map((txt, index) => <p key={index}>{txt}</p> )
      }
    </form>
  )
}

const App = () => (<Test3 />)

export default App
