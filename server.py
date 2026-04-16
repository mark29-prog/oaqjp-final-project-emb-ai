"""
Flask server for Emotion Detection application.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """
    Render the home page.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detection():
    """
    Handle emotion detection requests and return formatted response.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    dominant_emotion = result.get("dominant_emotion")

    # Handle invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    anger = result.get("anger")
    disgust = result.get("disgust")
    fear = result.get("fear")
    joy = result.get("joy")
    sadness = result.get("sadness")

    response_text = (
        "For the given statement, the system response is "
        f"'anger': {anger}, "
        f"'disgust': {disgust}, "
        f"'fear': {fear}, "
        f"'joy': {joy}, "
        f"and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return response_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
