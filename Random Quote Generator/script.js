async function generateQuote() {
    try {
        const response = await fetch('https://api.quotable.io/random');
        const data = await response.json();
        document.getElementById('quote').innerText = data.content;
        document.getElementById('author').innerText = "- " + data.author;
    } catch (error) {
        console.error("Error fetching the quote:", error);
    }
}

// Generate a quote when the page loads
window.onload = generateQuote;
