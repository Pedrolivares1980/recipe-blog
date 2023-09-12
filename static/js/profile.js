document.addEventListener("DOMContentLoaded", function () {
  const deleteButtons = document.querySelectorAll(".delete-btn");

  // Function to display a flash message
  function flashMessage(message, type) {
    const flashDiv = document.createElement("div");
    flashDiv.className = `alert alert-${type} alert-dismissible flash-message`;
    flashDiv.innerHTML = `
      <div class="container">
        <ul class="list-unstyled">
          <li class="text-center">
            ${message}
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </li>
        </ul>
      </div>
    `;

    const flashContainer = document.querySelector(".flash-messages");
    flashContainer.appendChild(flashDiv);

    // Add click event listener to manually close the flash message
    flashDiv.querySelector(".close").addEventListener("click", () => {
      flashDiv.remove();
    });
  }

  deleteButtons.forEach((button) => {
    button.addEventListener("click", function (e) {
      e.preventDefault();
      const recipeId = this.getAttribute("data-recipe-id");

      const confirmed = confirm("Are you sure you want to delete this recipe?");

      if (confirmed) {
        fetch(`/delete_recipe/${recipeId}`, {
          method: "DELETE",
        })
          .then((response) => {
            if (response.status === 204) {
              const row = document.getElementById(`recipe-${recipeId}`);
              if (row) {
                row.style.display = "none";
              }

              flashMessage("Recipe deleted successfully.", "success");
            } else if (response.status === 401) {
              flashMessage("Unauthorized.", "danger");
            } else if (response.status === 404) {
              flashMessage("Recipe not found or unauthorized.", "danger");
            }
          })
          .catch((error) => {
            console.error("Error:", error);
          });
      }
    });
  });
});
