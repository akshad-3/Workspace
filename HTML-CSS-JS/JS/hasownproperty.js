let animal = {
    eats : true
}
let rabbit = {
    jumps : true,
    __proto__:animal
}
for (let prop in rabbit){
    let own = rabbit.hasOwnProperty(prop);

    if(own){
        console.log(`own : ${prop}`);
    }
    else{
        console.log(`inherited : ${prop}`);
    }
}