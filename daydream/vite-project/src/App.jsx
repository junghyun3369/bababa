import { useState } from "react"
import "./index.css"

function App() {
  const start = 0;
  const end = 4;
   const [model, setModel] = useState([])
   const [point, setPoint] = useState([2, 0])
  const model1 = [
    [1,0,0,0,1],
    [1,0,1,0,1],
    [0,0,0,0,0],
    [1,0,1,0,1],
    [1,0,0,0,1]
  ]
  const model2 = [
    [1,0,0,0,1],
    [1,1,0,1,1],
    [0,0,0,0,0],
    [1,1,0,1,1],
    [1,0,0,0,1]
  ]
  const model3 = [
    [0,1,0,1,0],
    [1,0,0,0,1],
    [0,0,0,0,0],
    [1,0,0,0,1],
    [0,1,0,1,0]
  ]
  function reset() {
    setPoint([2, 0 ])
  }
  function btn1() {
    reset()
    setModel(model1)
  }
  function btn2() {
    reset()
    setModel(model2)
  }
  function btn3() {
    reset()
    setModel(model3)
  }

  return (
      <main>
        <nav>
          <button type="button" id="1" onClick={btn1}>호출1</button>
          <button type="button" id="2" onClick={btn2}>호출2</button>
          <button type="button" onClick={btn3}>호출3</button>
        </nav>
        <selction>
        <ul>
          { 
            model?.map((li,index) => {
            return (
                <li key={index}>
                  { 
                    li?.map((div, i) => {
                      const bg = (div === 1) ? 'bg1' : 'bg2'
                      return (
                        <div className={bg} key={i}></div>
                      )
                    })
                  }
                </li>
              )
            })            
          }
      </ul>
      </selction>
    </main>
  )
}

export default App
