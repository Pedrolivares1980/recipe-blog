// Event listener for the DOMContentLoaded event
document.addEventListener("DOMContentLoaded", function () {
  // This function will run when the page has fully loaded

  // Function to display a flash message
  function flashMessage(message, type) {
    // Create a flash message element and display the message
    const flashDiv = document.createElement("div");
    flashDiv.className = `alert alert-${type} alert-dismissible`;
    flashDiv.textContent = message;

    // Insert the flash message into the document
    const flashContainer = document.querySelector(".flash-messages");
    flashContainer.appendChild(flashDiv);

    // Get the auto-dismiss time from the data-auto-dismiss attribute
    const autoDismissTime = parseInt(flashDiv.getAttribute("data-auto-dismiss"));
  }
});
