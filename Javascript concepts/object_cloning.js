let src = {
    age: 19,
    ht: 178,
    wt: 85
 };

 let src1 = {
    name: "Shibam",
    Degree:"BCA",
    College: "ECMT"
 }

// // object cloning and object cpying is not same things
// let dest = src; // means we are copying , not cloning.


// Method 1 : object cloning use spread (...) operator
let dest = {...src};
console.log("src : ", src);
console.log("dest : ", dest);

// Method 2 : using assign() method
let dest1 = Object.assign({}, src);
console.log("src : ", src);
console.log("dest1 : ", dest1);

let dest2 = Object.assign({}, src, src1);
console.log("dest2 : ", dest2);

// read about Garbage collector shortly