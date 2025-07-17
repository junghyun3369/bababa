import {useState, useEffect} from 'react';

const App3Sub = ({txt, fnEvent}) => {
    return (
        <>
            <h3>자식영역</h3>
            <input type='text' value={txt} onChange={e => fnEvent(e.target.value)} />
        </>
    )
}

const App3Sub2 = () => {
    const [cnt,setCnt] = useState(0)
    useEffect(() => {
        console.log("useEffect")
        setCnt(cnt + 1)
    }, [])
    return (
        <>
         <h3>두번째 자식영역</h3>
         <p>{cnt}</p>
        </>
    )
}

const App3 = () => {
    const [txt, setText] = useState("")
    const [show, isshow] = useState(true)
    return (
        <>
            <h1>부모 영역 : {txt}</h1>
            <button type='button' onClick= {() => isshow(!show)}>버튼</button>
            { show && < App3Sub fnEvent={setText} txt={txt} />}
            { !show && < App3Sub2 />}
        </>
    )
}

export default App3
