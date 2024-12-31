document.addEventListener("DOMContentLoaded", () => {
    // Hide the animation container and show the content after 3.5 seconds
    setTimeout(() => {
      document.getElementById("animation-container").style.display = "none";
      document.getElementById("content").style.display = "block";
    }, 3500); // Adjust delay as needed
  });
  