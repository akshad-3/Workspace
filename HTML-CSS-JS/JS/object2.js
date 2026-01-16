// let user = {
//     name : "akshadd",
//     id:"233"
// }
// user.sayhi = function() {
//     console.log("hello world");
// }
// user.sayhi();
let user = {
  profile: {
    address: {
      city: "Mumbai"
    }
  }
};

console.log(user.profile?.address?.city);  // Mumbai
console.log(user.profile.contactz?.phone); // undefined

