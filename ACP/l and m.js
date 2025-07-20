// Generate and print a random set of numbers using a loop
console.log("Random set of numbers:");
for (let i = 0; i < 5; i++) {
    let randomNumber = Math.random() * 100; // Random number between 0 and 100
    console.log(Number ${ i + 1}: ${ randomNumber.toFixed(2) });
}

// Print the current date
let currentDate = new Date();
console.log("\nCurrent date:", currentDate.toLocaleDateString());

// Generate and print a rounded random number
let roundedRandomNumber = Math.round(Math.random() * 100); // Random number between 0 and 100, rounded
console.log("\nRounded random number:", roundedRandomNumber);
