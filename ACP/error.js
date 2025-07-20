try {
    // Code that might throw an error
    throw new Error("Something went wrong!");
} catch (error) {
    // Code to handle the error
    console.log("Error caught:", error.message);
}