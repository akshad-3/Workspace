import Header from "./component/Header"
import Entry from "./component/Entry"
import dataset from "./data"
export default function App(){
    const sorteddata = dataset.map((places)=>(<Entry 
        key={places.id}
        places={places}
        // src={places.img.src}
        // alt={places.img.alt}
        // title={places.title}
        // country={places.country}
        // googleMapsLinks={places.googleMapsLinks}
        // dates={places.dates}
        // text={places.text} 
        />
    ))
    return(
        <>
            <Header />
            {sorteddata}
        </>
        
    )
}