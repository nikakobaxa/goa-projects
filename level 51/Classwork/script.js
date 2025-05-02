// const div = document.getElementById("div");
// let x = 0;
// let y = 0;

// const moveRight = setInterval(() => {
//     x += 5;
//     div.style.left = `${x}px`;
//         if (x === 400) {
//             clearInterval(moveRight)
//             const moveDown = setInterval(() => {
//                 y += 5;
//                 div.style.top = `${y}px`
//                 if (y === 400) {
//                     clearInterval(moveDown)
//                     const moveLeft = setInterval(() => {
//                         x -= 5;
//                         div.style.left = `${x}px`;
//                         if (x === 0) {
//                             clearInterval(moveLeft)
//                             const moveUp = setInterval(() => {
//                                 y -= 5;
//                                 div.style.top = `${x}px`;
//                                 if (y === 0) {
//                                     clearInterval(moveUp)
//                                 }
//                             }, 20)
//                         }
//                     }, 20)
//                 }
//             }, 20)
//         }
// }, 20)


const div = document.getElementById("div");
let x = 0;
let y = 0;
let direction = "right";

const speed = 5;

const move = setInterval(() => {
    if (direction === "right") {
        x += speed;
        div.style.left = `${x}px`;
        if (x >= 400) {
            direction = "down";
        }
    } else if (direction === "down") {
        y += speed;
        div.style.top = `${y}px`;
        if (y >= 400) {
            direction = "left";
        }
    } else if (direction === "left") {
        x -= speed;
        div.style.left = `${x}px`;
        if (x <= 0) {
            direction = "up"
        }
    } else if (direction === "up") {
        y -= speed;
        div.style.top = `${y}px`;
        if (y <= 0) {
            direction = "right"
        }
    }
}, 20)