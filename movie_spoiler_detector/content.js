async function detectSpoilers() {
    const elements = document.querySelectorAll("p, span, li");

    for (let el of elements) {
        const text = el.innerText;
        if (!text || text.split(" ").length < 5) continue;

        try {
            const response = await fetch("http://127.0.0.1:5000/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ text: text })
            });

            const data = await response.json();

            if (data.is_spoiler) {
                el.style.filter = "blur(4px)";
                el.title = "Spoiler hidden. Hover to reveal.";
            }
        } catch (err) {
            console.error("Error calling spoiler detection API:", err);
        }
    }
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "detect_spoilers") {
        detectSpoilers();
        sendResponse({ status: "Spoiler detection triggered" });
    }
});
