let but = document.getElementById("button");
let but1 = document.getElementById("button1");
let but2 = document.getElementById("button2");

but.addEventListener('click', function(event){
    event.preventDefault()

    but.textContent = "Hello world"

    but.style.backgroundColor = "red"
})

but1.addEventListener('click', function(event){
    event.preventDefault()

    but1.textContent = "gamarjoba"

    but1.style.backgroundColor = "black"
})

but2.addEventListener('click', function(event){
    event.preventDefault()

    but2.textContent = "naxvamdis"

    but2.style.backgroundColor = "green"
})

function Changetext(){
    let but3 = document.getElementById("button3");

    but3.innerHTML = "Click me"

    but3.style.fontSize = "30px"
}

function Changecolor(){
    let but4 = document.getElementById("button4");

    but4.innerHTML = "Press me"

    but4.style.fontSize = "25px"
}



let num = ["apple", "banana", "orange"]

num.push("watermelon")

console.log(num)



let num1 = ["BMW", "MERCEDES", "PORSHE"]

num1.splice(2,1,  "TOYOTA")

console.log(num1)


let num2 = ["BMW", "MERCEDES", "PORSHE"]

num2.pop()
num2.shift()

console.log(num2)