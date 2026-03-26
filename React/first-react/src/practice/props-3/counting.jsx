import React from "react";

export default function counter(){
    return(
        <main>
            <h1>this is the thing that count</h1>
            <button className="minus" aria-label="area-decrease">-</button>
            <h2 className="count">0</h2>
            <button className="plus" aria-label="area-increase">+</button>
        </main>
    )
}