let para = document.getElementById("p");
let but = document.getElementById("but");
let but1 = document.getElementById("but1");

para.addEventListener('click', function(event){
    event.preventDefault()

    para.textContent = "Hello world"
})

but.addEventListener('click', function(event){
    event.preventDefault()

    but.style.fontSize = "30px"
})

let num = ["BMW", "MERCEDES", "PORSHE"]

num.pop()
num.shift()

console.log(num)

// 1. pop() - მასივიდან (Array) ბოლო ელემენტს შლის და აბრუნებს მას
// 2. shift() - მასივიდან პირველ ელემენტს შლის და აბრუნებს მას
// 3. textContent - აბრუნებს ან ცვლის HTML ელემენტის ტექსტურ შემცველობას (ტეგების გარეშე)
// 4. innerHTML - აბრუნებს ან ცვლის HTML ელემენტის შიდა კოდს (ტეგებთან ერთად)
// 5. DOM (Document Object Model) - დოკუმენტის ობიექტური მოდელი, რომელიც HTML-სა და JavaScript-ს შორის კავშირის საშუალებას იძლევა

