let maps = new Map([["a1","akshad"],["a2","akash"]]);
maps.set("a1","akash ")
console.log(maps);

//for an itreation of the map we can use the for looop

for(let [key,value] of maps){
    console.log(`key : ${key} and value : ${value}`);
}

//by using the ForEach() prototyoe

maps.forEach((kay,value)=>{
    console.log(kay,value);
})