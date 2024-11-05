// Function to display the uploaded photo
function displayPhoto(event) {
    const photoDisplay = document.getElementById("photo-display");
    const file = event.target.files[0];
    const reader = new FileReader();
    
    reader.onload = function() {
        photoDisplay.src = reader.result;
        photoDisplay.style.display = 'block';
    };
    
    if (file) {
        reader.readAsDataURL(file);
    }
}

// Function to submit the opinion
function submitOpinion() {
    const opinionInput = document.getElementById("opinion-input").value;
    const confirmationMessage = document.getElementById("confirmation-message");
    
    if (opinionInput.trim() === "") {
        confirmationMessage.style.color = "red";
        confirmationMessage.textContent = "Please write your opinion before submitting.";
    } else {
        confirmationMessage.style.color = "green";
        confirmationMessage.textContent = "Thank you for sharing your thoughts!";
    }
    
    // Clear the textarea
    document.getElementById("opinion-input").value = "";
}
