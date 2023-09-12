function toggleRecipeDetails(index) {
  const detailsDiv = document.getElementById(`recipe-details-${index}`);
  if (detailsDiv.style.display === "none") {
      detailsDiv.style.display = "block";
  } else {
      detailsDiv.style.display = "none";
  }
}

document.getElementById("difficulty-filter").addEventListener("change", function () {
  const selectedDifficulty = this.value;
  const recipeCards = document.querySelectorAll(".card");

  recipeCards.forEach(function (card) {
      const cardDifficulty = card.querySelector(".card-text").textContent.split(":")[1].trim().toLowerCase();

      if (selectedDifficulty === "all" || cardDifficulty === selectedDifficulty) {
          card.style.display = "block";
      } else {
          card.style.display = "none";
      }
  });
});

document.querySelectorAll(".view-details").forEach(function (button) {
  button.addEventListener("click", function () {
      const index = this.getAttribute("data-index");
      toggleRecipeDetails(index);
  });
});
