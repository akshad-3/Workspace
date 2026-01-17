let details1 = {
    firstname : "akshad",
    lastname : "patil",
    printname : function (){
        console.log(this.firstname + " " + this.lastname);
    }
}
details1.printname();
let details2 = {
    firstname : "akash",
    lastname :"gaikwad"
}
details1.printname.call(details2)

//above we used the function in object and used the same function for the another object 

//below we are going to make the fuction separete and use for any object this is proper way to do it 

let printname1 = function (state,city){
        console.log(this.firstname + " " + this.lastname + " state : " + state + " city " + city);
    }
let details3 = {
    firstname : "akshad",
    lastname : "patil"
};

let details4 = {
    firstname : "akash",
    lastname :"gaikwad"
};

printname1.call(details3,"maharashtra","latur");
printname1.apply(details3,["maharashtra","latur"]);

let copyoftheprintname = printname1.bind(details3,"maharashtra","latur");

console.log(copyoftheprintname);
copyoftheprintname();