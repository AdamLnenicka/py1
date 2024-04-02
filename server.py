"""
This module implements a Flask web application for emotion detection.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detection_route():
    """
    Endpoint for emotion detection.

    Accepts a POST request with JSON payload containing text to analyze.
    Returns emotion analysis results in JSON format.
    """
    data = request.get_json()
    text_to_analyze = data.get('text', '')
    result = emotion_detector(text_to_analyze)
    if result["dominant_emotion"] is None:
        return jsonify("Invalid text! Please try again.")
    response = {
        "anger": result["anger"],
        "disgust": result["disgust"],
        "fear": result["fear"],
        "joy": result["joy"],
        "sadness": result["sadness"],
        "dominant_emotion": result["dominant_emotion"]
    }
    response_str = ("For the given statement, the system response is "
                    f"'anger': {response['anger']}, "
                    f"'disgust': {response['disgust']}, "
                    f"'fear': {response['fear']}, "
                    f"'joy': {response['joy']} and "
                    f"'sadness': {response['sadness']}. "
                    f"The dominant emotion is {response['dominant_emotion']}.")
    return jsonify(response_str)

if __name__ == '__main__':
    app.run(debug=True)
