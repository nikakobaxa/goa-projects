// const div = document.getElementById("div");
// let x = 0;
// let y = 0;
// let direction = "right";

// const speed = 5;

// const move = setInterval(() => {
//     if (direction === "right") {
//         x += speed;
//         div.style.left = `${x}px`;
//         if (x >= 400){
//             direction = "up";
//         }
//     } else if (direction === "up") {
//         y -= speed;
//         div.style.top = `${y}px`;
//         if (y <= 0) {
//             direction = "left";
//         }
//     } else if (direction === "left") {
//         x -= speed;
//         div.style.left = `${x}px`;
//         if (x <= 0) {
//             direction = "down";
//         }
//     } else if (direction === "down") {
//         y += speed;
//         div.style.top = `${y}px`;
//         if (x >= 400) {
//             direction = "right"
//         }
//     }
       

// }, 20);

const div1 = document.getElementById("div1");
const  moveAmount = 20;
let x = 0;
let y = 0;

document.addEventListener("keydown", event => {
    
    if (event.key.startsWith("Arrow")){
        event.preventDefault();

        switch(event.key){
            case "ArrowUp":
            y -= moveAmount;
            break;
            case "ArrowDown":
            y += moveAmount;
            break;
            case "ArrowLeft":
            x -= moveAmount;
            break;
            case "ArrowRight":
            x += moveAmount;
            break;
        }
        
        div1.style.top = `${y}px`;
        div1.style.left = `${x}px`;

    }


})