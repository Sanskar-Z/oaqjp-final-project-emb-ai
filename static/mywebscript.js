async function RunSentimentAnalysis() {
    const text = document.getElementById("textToAnalyze").value.trim();
    const output = document.getElementById("system_response");

    if (!text) {
        output.textContent = "Invalid input! Please enter some text to analyze.";
        return;
    }

    output.textContent = "Analyzing...";

    try {
        const response = await fetch(
            "/emotionDetector?textToAnalyze=" + encodeURIComponent(text)
        );

        const result = await response.text();

        if (!response.ok) {
            output.textContent = result;
            return;
        }

        output.textContent = result;
    } catch (error) {
        output.textContent = "Unable to connect to the emotion detection server.";
    }
}
