const img = document.getElementById("img")
const next = document.getElementById("next")
const prev = document.getElementById("prev")

let i = 0;
const images = ["./images1.png", "./images2.png", "./images3.png", "./images4.png", "./images5.png"]

next.addEventListener("click", function(){
    i++;
    if (i >= images.lenght){
        i = 0;
    }
    img.src = images[i];
})

prev.addEventListener("click", function(){
    i--;
    if (i <= -1){
        i = images.length - 1;
    }
    img.src = images[i];
})

document.getElementById("parent").addEventListener("click", function(){
    console.log("red")
})

document.getElementById("child").addEventListener("click", function(){
    console.log("blue")
})

document.getElementById("parent1").addEventListener("click", function(){
    console.log("red")
}, true);

document.getElementById("child1").addEventListener("click", function(){
    console.log("blue")
}, true);