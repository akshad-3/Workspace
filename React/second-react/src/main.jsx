import {createRoot} from "react-dom/client"
import Header from "./Header"
import MainContent from "./MainContent"
import Footer from "./Footer"
import example from "./example"
const root = createRoot(document.getElementById('root'))

function Page() {
    return (
        <>
        <Header/>
        <MainContent />
        <Footer />
        <example />
        </>
    )
}
root.render(
    <Page />
)

