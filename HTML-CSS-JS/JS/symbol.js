let id = Symbol("id");
let user = {
    name : "akshad",
    rollno : 23,
    [id]:123
};

for (let key in user)
    console.log(key);

console.log(user[id])