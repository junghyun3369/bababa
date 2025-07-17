import { BrowserRouter, Routes, Route, useParams, useSearchParams} from "react-router"

const Page1 = () => {
  const parmas = useParams()
  const [sParam] = useSearchParams()
  //console.log(parmas.txt, sParam.get('no'))
  return (
    <>
    <h1>페이지1</h1>
    <p>{parmas.txt}</p>
    <p>{sParam.get('no')}</p>
    </>
  )
}
const Page2 = () => {
  return (
    <h1>페이지2</h1>
  )
}
const Page = () => {
  return (
    <h1>기본 화면</h1>
  )
}
const App4 = () => {
    return (
      <BrowserRouter>
        <Routes>
           <Route path="/Page1/:txt" element={<Page1 />} />
           <Route path="/Page2" element={<Page2 />} />
           <Route path="*" element={<Page />} />
        </Routes>
      </BrowserRouter>
    )
}
export default App4