// Asynchronous function simulating an API call
async function fetchData() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({ name: "John", age: 30 }); // Example JSON data
        }, 2000); // 2-second delay
    });
}

// Function dependent on fetchData's result
async function dependentFunction() {
    try {
        const data = await fetchData(); // Wait for fetchData to resolve
        console.log("Fetched Data:", data);
        return Name: ${ data.name }, Age: ${ data.age };
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

// Call the dependent function
dependentFunction().then((result) => console.log(result));