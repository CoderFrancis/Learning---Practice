function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
}

document.addEventListener('DOMContentLoaded', function() {
    // Add JavaScript code here
});

document.addEventListener('DOMContentLoaded', function() {
    const darkModeToggle = document.getElementById('darkModeToggle');
    
    // Check if the user has a preference for dark mode
    const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");
    
    // Check if the user has already selected dark mode earlier
    const currentTheme = localStorage.getItem("theme");
    
    if (currentTheme == "dark" || (currentTheme === null && prefersDarkScheme.matches)) {
        document.documentElement.setAttribute("data-theme", "dark");
        darkModeToggle.checked = true;
    } else {
        document.documentElement.setAttribute("data-theme", "light");
    }
    
    // Listen for a click on the toggle button
    darkModeToggle.addEventListener('change', function() {
        if (darkModeToggle.checked) {
            document.documentElement.setAttribute("data-theme", "dark");
            localStorage.setItem("theme", "dark");
        } else {
            document.documentElement.setAttribute("data-theme", "light");
            localStorage.setItem("theme", "light");
        }
    });
});