document.addEventListener("DOMContentLoaded", () => {
  const switchInput = document.getElementById("themeSwitch");

  // Sync toggle state with current theme (class already applied by head script)
  if (switchInput) {
    switchInput.checked = document.documentElement.classList.contains("dark");
  }

  // Initialize Lucide icons
  if (typeof lucide !== "undefined") {
    lucide.createIcons();
  }

  // Handle theme toggle logic
  if (switchInput) {
    switchInput.addEventListener("change", () => {
      if (switchInput.checked) {
        document.documentElement.classList.add("dark");
        localStorage.setItem("theme", "dark");
      } else {
        document.documentElement.classList.remove("dark");
        localStorage.setItem("theme", "light");
      }
      if (typeof lucide !== "undefined") lucide.createIcons();
    });
  }

  // Handle Direction Toggle Logic
  const dirToggle = document.getElementById("dirToggle");
  if (dirToggle) {
    // Initial sync
    const currentDir = document.documentElement.dir || "ltr";
    dirToggle.querySelector("span").innerText = currentDir.toUpperCase();

    dirToggle.addEventListener("click", () => {
      // Add animation class
      document.documentElement.classList.add("dir-switching");

      // Short delay for the blur to start
      setTimeout(() => {
        const isRTL = document.documentElement.dir === "rtl";
        const newDir = isRTL ? "ltr" : "rtl";

        document.documentElement.dir = newDir;
        localStorage.setItem("dir", newDir);
        dirToggle.querySelector("span").innerText = newDir.toUpperCase();

        if (typeof lucide !== "undefined") lucide.createIcons();

        // Remove animation class after the switch is done
        setTimeout(() => {
          document.documentElement.classList.remove("dir-switching");
        }, 150); // Match with app.css body transition
      }, 100);
    });
  }

  // Back to Top Logic
  const backToTop = document.createElement("button");
  backToTop.className = "back-to-top";
  backToTop.innerHTML = '<i data-lucide="arrow-up"></i>';
  document.body.appendChild(backToTop);

  // Re-create icons to catch the new arrow-up
  if (typeof lucide !== "undefined") {
    lucide.createIcons();
  }

  window.addEventListener("scroll", () => {
    if (window.scrollY > 400) {
      backToTop.classList.add("visible");
    } else {
      backToTop.classList.remove("visible");
    }
  });

  backToTop.addEventListener("click", () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  });
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
