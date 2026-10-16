
"""Flask web server for the Emotion Detector application."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the main emotion detection page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    """Detect emotions in submitted text and return formatted results."""
    text_to_analyze = request.values.get("textToAnalyze", "").strip()

    if not text_to_analyze:
        return "Invalid input! Please enter some text to analyze.", 400

    result = emotion_detector(text_to_analyze)

    if result is None:
        return (
            "Emotion detection service is unavailable. Please try again.",
            502,
        )

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
