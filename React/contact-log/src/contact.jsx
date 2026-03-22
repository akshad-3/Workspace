import catimage1 from "/Users/akshad/GitHub/Workspace/React/contact-log/src/assets/cat.jpeg"
import phoneimage1 from "/Users/akshad/GitHub/Workspace/React/contact-log/src/assets/phone.png"
import mailimage1 from "/Users/akshad/GitHub/Workspace/React/contact-log/src/assets/mail.png"

export default function Contact(props){
    console.log(props)
    return(
        <article className="contact-card">
            <img
                src={props.img}
                alt="Photo of Mr. Whiskerson"
            />
            <h3>{props.name}</h3>
            <div className="info-group">
                <img
                    src={props.phoneimage1}
                    alt="phone icon"
                />
                <p>{props.phone}</p>
            </div>
            <div className="info-group">
                <img
                    src={props.mailimage1}
                    alt="mail icon"
                />
                <p>{props.email}</p>
            </div>
        </article>
    )
}