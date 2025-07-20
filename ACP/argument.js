// Task 1: Function to sum arguments
function sumArguments(...args) {
    return args.reduce((total, num) => total + num, 0);
}

console.log("Sum of arguments:", sumArguments(1, 2, 3, 4, 5));

// Task 2: Print trigonometric degrees
function printTrigonometricDegrees(degrees) {
    let radians = degrees * (Math.PI / 180);
    console.log(Sine of ${ degrees } degrees:, Math.sin(radians));
    console.log(Cosine of ${ degrees } degrees:, Math.cos(radians));
    console.log(Tangent of ${ degrees } degrees:, Math.tan(radians));
}

printTrigonometricDegrees(30);
