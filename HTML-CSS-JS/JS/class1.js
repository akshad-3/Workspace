class class1 {
    constructor (name){
        this.yourname=name;
    }
    sayhi(){
        console.log(this.yourname);
    }

}
let user = new class1("akshad");
user.sayhi();
