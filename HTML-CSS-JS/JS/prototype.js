let animal ={
    eats : true,
    walk(){
        console.log("this animal is walking");
    }
};
let rabbit ={
    jumps : true,
    __proto__:animal
};
let color ={
    color: "white",
    __proto__:rabbit
}
color.walk();
console.log(color.jumps)
console.log(color.color)
