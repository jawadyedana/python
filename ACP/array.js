// Create an array
let originalArray = [1, 2, 3, 4, 5];

// Map it with a number (let's say multiply by 2)
let mappedArray = originalArray.map(num => num * 2);

// Sort in ascending order
let ascendingOrder = [...mappedArray].sort((a, b) => a - b);

// Sort in descending order
let descendingOrder = [...mappedArray].sort((a, b) => b - a);

console.log("Mapped Array:", mappedArray);
console.log("Ascending Order:", ascendingOrder);
console.log("Descending Order:", descendingOrder);
