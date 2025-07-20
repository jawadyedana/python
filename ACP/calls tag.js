// Create an object
let book = {
    title: "The Adventure",
    author: "Jane Doe",
    genres: ["Fiction", "Thriller", "Mystery"]
};

// Create an array
let numbers = [10, 20, 30, 40];

// Display values using object keys
console.log("Book title:", book.title);
console.log("Book author:", book.author);

// Display values using array index
console.log("First number:", numbers[0]);

// Display whole array using join
console.log("Genres:", book.genres.join(", "));
console.log("Numbers:", numbers.join(" - "));

// Use pop function
console.log("Popped genre:", book.genres.pop());
console.log("Genres after pop:", book.genres.join(", "));
