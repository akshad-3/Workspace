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