//we also can make a object using a contructor whcih use singleton
//the singleton does not form by literal syntax
/*So this is the basic object syntax that we use 
    to creat a object.
    IMPORTANT!!!!
    class = car design
    object = actual car

    This is called a Obect Litaral!!
*/
const student={
    name:"akshad",
    roll:100,
    age:23,
    email:"akshad@gmail.com"

}

//this is a singoletone object declaration

const userdata=new Object();
console.log(userdata)

const example1={
    userdetail:{
        username:{
            username:"akshad",
            userage:23
        }
    }
}
console.log(example1.userdetail.username.userage);

//here is how to copy a object into another object 
let user = {
    name : "akshad",
    id:"23"
}
let exm ={}
for(let key in user ){
    exm[key] = user[key];
}
exm.name="akash";
alert(exm.name);

//copy the object using object.assign
let user1 = {
    name : "akshad",
    id :23
};
let assingment1 ={class:"forth"};
let assingment2 ={sem:"first"};

Object.assign(user1,assingment1,assingment2);

console.log(user1.sem);