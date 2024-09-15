let arr = [10, 15, 20, 25, 30, 35, 40]

arr.shift(); //* remove left most element
arr.unshift("Shibam") //* add element at first 

console.log(arr);

console.log(arr.slice(2,4));

//! splice() methode:
// we can insert, replace, remove from/in array
// splice("start", "no. of elem to be removed", "replace")
arr.splice(1,2,"Sadhukhan");
console.log(arr);





//! MAP, FILTER, REDUCE;

//* Map
let nums = [10, 20, 30, 25, 35, 45]
// exmpl 1
let ans = nums.map((val) => {
    return val*val;
})
console.log(ans);
// exmpl 2
nums.map((val, idx) => {
    console.log(val*10);
    console.log(idx);
})



//* Filter
let even = nums.filter((val) => {
    return val%2 === 0;
})
console.log(even);



//* Reduce

let sum = nums.reduce((acc, curr) => {
    return acc + curr;
}, 0);

console.log(sum);


//! forEach, for-of, for-in loop;

// forEach
let num = [10, 12, 14, 13, 16, 15]
console.log(num);

num.forEach((val, idx) => {
    console.log("number : ", val, "Index : ", idx);
})




// for-of loop
let nickName = "shibam";

for(let ch of nickName) {
    console.log(ch);
}

let numbers = [55, 65, 43, 85]

for(let val of numbers) {
    console.log(val);
}




// for in 
let obj = {
    name : "Shibam",
    age : 19,
    height : 5.8
};

for(key in obj) {
    console.log(key);
}

for(key in obj) {
    console.log(key, "->", obj[key]);
}