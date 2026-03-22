export default function Entry(props){
    return(
        <article className="journal-entry">
            <div>
                <img className="main-image" src={props.img.src} alt={props.img.alt} />
            </div>
            <div className="info-container">
                <img className="ping-image" src={props.pingImage} alt="ping" />
                <span className="country" >{props.countryName}</span>
                <a href={props.countryLocation}>view on Google map</a>
                <h2 className="entry-title">{props.countryTitle}</h2>
                <p className="entry-date">{props.countryDate}</p>
                <p className="entry-txt">{props.countryDisciption}</p>
            </div>

        </article>
    )
}