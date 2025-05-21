const img = document.getElementById("img");
const next = document.getElementById("next");
const prev = document.getElementById("prev");

let i = 0;
const images = ["./images1.png", "./images2.png", "./images3.png", "./images4.png", "./images5.png"]

next.addEventListener("click", function(){
    i++;
    if (i >= images.length){
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

const form = document.getElementById("form");

form.addEventListener("submit", function(e){
    e.preventDefault();
    console.log(form.elements.name.value);
})