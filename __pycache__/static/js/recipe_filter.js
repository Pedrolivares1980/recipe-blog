document.addEventListener("DOMContentLoaded", function () {
  // Get references to the filter elements
  const difficultyFilter = document.getElementById("difficulty-filter");
  const categoryFilter = document.getElementById("category-filter");

  // Add change event listeners to the filter elements
  difficultyFilter.addEventListener("change", filterRecipes);
  categoryFilter.addEventListener("change", filterRecipes);

  // Function to filter recipes based on selected filters
  function filterRecipes() {
    // Get the selected difficulty and category values
    const selectedDifficulty = difficultyFilter.value.toLowerCase();
    const selectedCategory = categoryFilter.value;

    // Get all recipe cards
    const recipeCards = document.querySelectorAll(".recipe-card");

    // Iterate through each recipe card
    recipeCards.forEach((card) => {
      // Get the difficulty and category attributes of the card
      const cardDifficulty = card.getAttribute("data-difficulty").toLowerCase();
      const cardCategory = card.getAttribute("data-category");

      // Determine if the card should be visible based on selected filters
      const isVisible = (
        (selectedDifficulty === "all" || cardDifficulty === selectedDifficulty) &&
        (selectedCategory === "all" || cardCategory === selectedCategory)
      );

      // Set the display style of the card
      card.style.display = isVisible ? "block" : "none";
    });
  }
});
