export default function Jokes(props){
    return(
        <>
            <p>{props.setup}</p>
            <p>{props.punchline}</p>
            
            <p>{props.isfun}</p>
            <p>{props.comments}</p>
            <hr />
        </>
    )
}