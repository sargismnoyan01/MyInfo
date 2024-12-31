document.addEventListener("DOMContentLoaded", () => {
    // Hide the animation container after 2 seconds
    setTimeout(() => {
      const animationContainer = document.getElementById("animation-container");
      const content = document.getElementById("content");
      animationContainer.style.display = "none";
      content.style.display = "block";
    }, 2000); // 2000 milliseconds = 2 seconds
  });
  