import ReactDOM from 'react-dom/client';

export default function example(){
    return(
        <h1>current time is about {new Date().getHours % 12}</h1>
    )
}
ReactDOM.createRoot(document.getElementById('newroot')).render(<example />);