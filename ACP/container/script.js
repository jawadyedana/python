function showHobby(hobby) {
    const hobbyDescription = document.getElementById("hobbyDescription");

    let content = "";
    switch (hobby) {
        case "coding":
            content = "I love coding and building web applications. I spend most of my free time learning new technologies.";
            break;
        case "photography":
            content = "Photography helps me see the world from a different perspective. I enjoy nature and urban photography.";
            break;
        case "traveling":
            content = "Traveling allows me to explore new cultures, cuisines, and landscapes. It's a refreshing escape from routine.";
            break;
        case "music":
            content = "Music is a powerful form of expression. I enjoy both listening and playing musical instruments like guitar.";
            break;
        default:
            content = "Click on a hobby card to see more details.";
    }

    hobbyDescription.textContent = content;
    document.getElementById("hobbyDetail").scrollIntoView({ behavior: "smooth" });
}
