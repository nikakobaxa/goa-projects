let score = 25;

if (score >= 90 && score <= 100){
    console.log("A");
} else if (score >= 80 && score < 90){
    console.log("B");
} else if (score >= 70 && score < 80){
    console.log("C");
} else {
    console.log("D");
}

function checkAge(age){
    if (age < 13){
        console.log("You are kid");
    } else if (age >= 13 && age < 18){
        console.log("You are not adult yet"); 
    } else {
        console.log("you are adult")
    }   
} 

let num = 5 
while (num <= 20) {
    console.log(num)
    num++;
}

for (let i = 0; i <= 100; i++){
    console.log(i);
}

for (let i = 50; i <= 100; i += 2){
    console.log(i);
}