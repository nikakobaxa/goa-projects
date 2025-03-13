const form = document.getElementById("form");


//form.addEventListener('submit', function(event){
    //event.preventDefault();

    //const radioRes = form.elements.m1;

    //console.log(radioRes.value);
//})

//form.addEventListener('submit', function(event){
    //event.preventDefault();

    //const radioRes = form.elements.checkbox;

    //console.log(radioRes.checked)
//})

form.addEventListener('submit', function(event){
    event.preventDefault();

    const dropDownmenu = form.elements.dropDown.value;

    console.log(dropDownmenu);
})

const s1 = 5
const s2 = 5

console.log(s1 > s2)
console.log(s1 < s2)
console.log(s1 >= s2)
console.log(s1 <= s2)
console.log(s1 == s2)
console.log(s1 === s2)
console.log(s1 != s2)
console.log(s1 !== s2)