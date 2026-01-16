let myarray = [1,2,3,4];

let obj = new Set(myarray);
obj.add(5);
console.log(obj.size);

let obj1 = {name : "akshad"};
obj.add(obj1);
console.log(obj);


//The Weakset in the sets 

let weakset = new WeakSet();
let ob1 = {
    name : "akshad"
};
let ob2 = {};

weakset.add(ob1,ob2);
console.log(weakset);
