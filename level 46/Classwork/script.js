let but = document.getElementById("button");
let but1 = document.getElementById("button1");
let para = document.querySelector("p");

but.addEventListener('click', function(event){
    event.preventDefault()

    but.textContent = "Hello world"

    but.style.backgroundColor = "red"
})

but1.addEventListener('click', function(event){
    event.preventDefault()

    but1.style.color = "Green"

    but1.textContent = "gamarjoba"
})

console.log(para.textContent)

function Changetext(){
    let but2 = document.getElementById("button2");

    but2.innerHTML = "Click me"   
}

function Changecolor(){
    let but3 = document.getElementById("button3");

    but3.style.fontSize = "30px"
}

