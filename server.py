"""Flask web application for the Emotion Detector project."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the main page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_route():
    """Analyze submitted text and return its emotion scores."""
    text_to_analyse = request.values.get("textToAnalyze", "").strip()

    if not text_to_analyse:
        return "Invalid text! Please try again!", 400

    result = emotion_detector(text_to_analyse)

    if result["dominant_emotion"] is None:
        return "Emotion analysis is currently unavailable. Please try again.", 503

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
