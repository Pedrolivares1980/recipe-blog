document.addEventListener("DOMContentLoaded", function () {
  const difficultyFilter = document.getElementById("difficulty-filter");
  const categoryFilter = document.getElementById("category-filter");

  difficultyFilter.addEventListener("change", filterRecipes);
  categoryFilter.addEventListener("change", filterRecipes);

  function filterRecipes() {
    const selectedDifficulty = difficultyFilter.value.toLowerCase(); // Convertir a minúsculas
    const selectedCategory = categoryFilter.value;

    const recipeCards = document.querySelectorAll(".recipe-card");

    recipeCards.forEach((card) => {
      const cardDifficulty = card.getAttribute("data-difficulty").toLowerCase(); // Convertir a minúsculas
      const cardCategory = card.getAttribute("data-category");

      const isVisible = (
        (selectedDifficulty === "all" || cardDifficulty === selectedDifficulty) &&
        (selectedCategory === "all" || cardCategory === selectedCategory)
      );

      card.style.display = isVisible ? "block" : "none";
    });
  }
});



