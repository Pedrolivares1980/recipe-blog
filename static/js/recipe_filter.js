document.addEventListener("DOMContentLoaded", function () {
  // Get references to the filter elements
  const difficultyFilter = document.getElementById("difficulty-filter");
  const categoryFilter = document.getElementById("category-filter");

  // Get all recipe cards
  const recipeCards = Array.from(document.querySelectorAll(".recipe-card"));

  // Function to filter and group recipes
  function filterAndGroupRecipes() {
    // Get the selected difficulty and category values
    const selectedDifficulty = difficultyFilter.value.toLowerCase();
    const selectedCategory = categoryFilter.value;

    // Filter the recipe cards and keep only visible ones
    const visibleRecipeCards = recipeCards.filter((card) => {
      const cardDifficulty = card.getAttribute("data-difficulty").toLowerCase();
      const cardCategory = card.getAttribute("data-category");

      return (
        (selectedDifficulty === "all" || cardDifficulty === selectedDifficulty) &&
        (selectedCategory === "all" || cardCategory === selectedCategory)
      );
    });

    // Clear the existing recipe groups
    const recipeGroupsContainer = document.getElementById("recipe-groups");
    recipeGroupsContainer.innerHTML = "";

    // Display the filtered and grouped recipes without spaces
    visibleRecipeCards.forEach((card) => {
      recipeGroupsContainer.appendChild(card);
    });
  }

  // Add change event listeners to the filter elements
  difficultyFilter.addEventListener("change", filterAndGroupRecipes);
  categoryFilter.addEventListener("change", filterAndGroupRecipes);

  // Initially, filter and group the recipes
  filterAndGroupRecipes();
});
