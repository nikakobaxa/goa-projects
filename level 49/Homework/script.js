const div = document.getElementById("container");

// setTimeout(function(){
//     console.log("Hello world")
// }, 1000)

// setInterval(function(){
//     console.log("Hello world");
// }, 1000)

// let i = 0

// setInterval(function(){
//     console.log(i);
//     i++;
// }, 1000)


let p = document.createElement("p");
let textnode = document.createTextNode("Hello world");
p.appendChild(textnode)
div.appendChild(p)

let button = document.createElement("button");
let textnode1 = document.createTextNode("Click me");
button.appendChild(textnode1)
div.appendChild(button)

div.removeChild(button)

let p1 = document.createElement("p1");
let textnode2 = document.createTextNode("Gamarhoba samyaro");
p1.appendChild(textnode2)
div.replaceChild(p1, p)
