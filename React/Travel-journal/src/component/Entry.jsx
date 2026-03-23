import ping from "../assets/PING.png"

export default function Entry(props){
    return(
        <article className="journal-entry">
            <div>
                <img className="main-image" src={props.places.img.src} alt={props.places.img.alt} />
            </div>
            <div className="info-container">
                <img className="ping-image" src={ping} alt="ping" />
                <span className="country" >{props.places.country}</span>
                <a href={props.places.googleMapsLinks}>view on Google map</a>
                <h2 className="entry-title">{props.places.title}</h2>
                <p className="entry-date">{props.places.dates}</p>
                <p className="entry-txt">{props.places.text}</p>
            </div>

        </article>
    )
}