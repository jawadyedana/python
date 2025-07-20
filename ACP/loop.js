let count = 0;
let numbers = [];

while (count < 5) {
    let randomNumber = Math.floor(Math.random() * 100); // Random number between 0 and 99
    numbers.push(randomNumber);
    count++;
}

console.log("Set of random numbers:", numbers);