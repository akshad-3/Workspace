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

rabbit.walk();
