// const fruits = ["ვაშლი", "მსხალი", "ბანანი"];

// for (const fruit of fruits) {
//   console.log(fruit);
// }

// for (const fruit in fruits) {
//    console.log(fruit);
// }

// const name = "nika"
// const age = 16

// const message = `hello, my name is ${name} and i am ${age} years old.`;
// console.log(message)

// fruits.forEach((el) => {
//     console.log(el);
// });

// fruits.forEach((fruit) => {
//     console.log(`i love ${fruits}`);
// });

// const user = {
//     name: "nika",
//     greet() {
//         console.log(`hello my name is ${this.name}`);
//     }
// };

// user.greet();

// const name = "nika";
// const age = 16;

// const user = {
//     name,
//     age
// };

// console.log(user)

const fullname = "Name"

const user = {
    [`first${fullname}`]: "nika",
    [`last${fullname}`]: "kobakhidze"
};

console.log(user);