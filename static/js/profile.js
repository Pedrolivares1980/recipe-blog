document.addEventListener('DOMContentLoaded', function () {
  // Get all delete buttons for recipes
  const deleteButtons = document.querySelectorAll('.delete-btn');

  // Add a click event listener to each delete button
  deleteButtons.forEach((button) => {
    button.addEventListener('click', function () {
      // Get the recipe ID from the data attribute
      const recipeId = this.getAttribute('data-recipe-id');

      // Send a DELETE request to the server
      fetch(`/delete_recipe/${recipeId}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.status === 'success') {
            // Successful deletion, display a success flash message
            const flashContainer = document.querySelector('.flash-messages');
            if (flashContainer) {
              flashContainer.innerHTML = `
                <div class="alert alert-success alert-dismissible text-center">
                  ${data.message}
                  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
              `;
            }

            // Hide the row of the deleted recipe
            const recipeRow = document.getElementById(`recipe-${recipeId}`);
            if (recipeRow) {
              recipeRow.remove();
            }
          } else {
            // Display an error flash message if needed
            const flashContainer = document.querySelector('.flash-messages');
            if (flashContainer) {
              flashContainer.innerHTML = `
                <div class="alert alert-danger alert-dismissible text-center">
                  ${data.message}
                  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
              `;
            }
          }
        })
        .catch((error) => {
          console.error('Error deleting the recipe:', error);
        });
    });
  });

  // Add an event listener to the delete account button
  const deleteAccountButton = document.getElementById("delete-account-btn");
  if (deleteAccountButton) {
      deleteAccountButton.addEventListener("click", function() {
          if (confirm("Are you sure you want to delete your account? This action cannot be undone.")) {
              // If the user confirms, redirect to the delete account route
              window.location.href = "/delete_account";
          }
      });
  }

});
