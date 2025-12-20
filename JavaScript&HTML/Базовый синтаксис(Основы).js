
let name = "Иван";      
const age = 25;         


function sayHello(person) {
    return "Привет, " + person + "!";
}
sayHello("Анна");


const add = (a, b) => a + b;
add(5, 3);  // 8

// Условия
if (age >= 18) {
    console.log("Совершеннолетний");
} else {
    console.log("Несовершеннолетний");
}


for (let i = 0; i < 5; i++) {
    console.log(i);
}