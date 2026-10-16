document.addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById("textToAnalyze");
    const button = document.getElementById("analyzeButton");
    const result = document.getElementById("result");

    button.addEventListener("click", async function () {
        const text = input.value.trim();

        if (!text) {
            result.textContent = "Invalid text! Please try again!";
            return;
        }

        result.textContent = "Analyzing...";

        try {
            const response = await fetch("/emotionDetector", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                body: new URLSearchParams({
                    textToAnalyze: text
                })
            });

            const message = await response.text();
            result.textContent = message;

        } catch (error) {
            result.textContent =
                "Unable to connect to the server. Please try again.";
        }
    });
});
