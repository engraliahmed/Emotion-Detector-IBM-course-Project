# pylint: disable=C0301, W0613, R0914, R0801, C0412
"""
This server.py file runs the Flask application for Emotion Detection.
It handles web requests and uses the emotion_detector function to analyze text.
"""
from flask import Flask, render_template, request
from emotion_detection import emotion_detector

# Flask application instance (APP is used for PyLint compliance)
APP = Flask("Emotion Detection")


@APP.route("/emotionDetector")
def sent_analyzer():
    """
    This function processes the text input from the web interface,
    calls the emotion detection logic, and formats the output for display.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        # Handling invalid/blank text input
        return "Invalid text! Please try again!"

    # Formatting the output string, broken up for readability
    output = f"For the given statement, the system response is 'anger': {response['anger']}, "
    output += f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
    output += f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
    output += f"The dominant emotion is {response['dominant_emotion']}."

    return output


@APP.route("/")
def render_index_page():
    """
    This function renders the main index page (index.html) of the application.
    """
    return render_template("index.html")


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000)
