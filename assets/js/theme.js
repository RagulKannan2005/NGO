document.addEventListener("DOMContentLoaded", () => {
  const switchInput = document.getElementById("themeSwitch");

  // Apply saved theme on load
  if (localStorage.getItem("theme") === "dark") {
    document.documentElement.classList.add("dark");
    if (switchInput) switchInput.checked = false; // "Dark" text visible (default switch state is unchecked in index.html for dark mode)
  } else if (localStorage.getItem("theme") === "light") {
    document.documentElement.classList.remove("dark");
    if (switchInput) switchInput.checked = true; // "Light" active
  } else {
    // default to dark if no theme is set
    document.documentElement.classList.add("dark");
    if (switchInput) switchInput.checked = false;
  }

  // Handle toggle logic
  if (switchInput) {
    switchInput.addEventListener("change", () => {
      if (switchInput.checked) {
        document.documentElement.classList.remove("dark");
        localStorage.setItem("theme", "light");
      } else {
        document.documentElement.classList.add("dark");
        localStorage.setItem("theme", "dark");
      }
    });
  }
});

// Hide loader on full page load
window.addEventListener("load", () => {
  const loader = document.getElementById("page-loader");
  if (loader) {
    // slight delay for visual smoothness
    setTimeout(() => {
      loader.classList.add("hidden");
    }, 400);
  }
});

