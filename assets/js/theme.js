document.addEventListener("DOMContentLoaded", () => {
  const themeToggles = document.querySelectorAll('.theme-toggle input[type="checkbox"], #themeSwitch');
  
  // Apply theme from localStorage immediately if not already handled by head script
  const currentTheme = localStorage.getItem("theme");
  if (currentTheme === "dark") {
    document.documentElement.classList.add("dark");
  } else if (currentTheme === "light") {
    document.documentElement.classList.remove("dark");
  }

  // Sync all toggle states
  const isDark = document.documentElement.classList.contains("dark");
  themeToggles.forEach(toggle => {
    toggle.checked = isDark;
  });

  // Handle theme toggle logic for all matched elements
  themeToggles.forEach(toggle => {
    toggle.addEventListener("change", () => {
      const shouldBeDark = toggle.checked;
      
      if (shouldBeDark) {
        document.documentElement.classList.add("dark");
        localStorage.setItem("theme", "dark");
      } else {
        document.documentElement.classList.remove("dark");
        localStorage.setItem("theme", "light");
      }

      // Sync other toggles on the page
      themeToggles.forEach(t => { if (t !== toggle) t.checked = shouldBeDark; });
      
      if (typeof lucide !== "undefined") lucide.createIcons();
    });
  });

  // Also support simple button/label toggles without inputs (using .theme-toggle class)
  const simpleToggles = document.querySelectorAll('.theme-toggle:not(input):not(:has(input))');
  simpleToggles.forEach(toggle => {
    toggle.addEventListener('click', () => {
      const isNowDark = document.documentElement.classList.toggle('dark');
      const newTheme = isNowDark ? 'dark' : 'light';
      localStorage.setItem('theme', newTheme);
      
      // Update any checkbox toggles
      themeToggles.forEach(t => t.checked = isNowDark);
      
      if (typeof lucide !== "undefined") lucide.createIcons();
    });
  });

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

    // Scroll-aware navbar
    const navbar = document.querySelector(".navbar");
    if (navbar) {
      if (window.scrollY > 60) {
        navbar.classList.add("scrolled");
      } else {
        navbar.classList.remove("scrolled");
      }
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
