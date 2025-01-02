"""
This module defines the Flash server for the Emotion Detection application
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotion_detector')
def emotion_detection_route():

    """ 
    Handles the emotion detection route.
    Retieves the 'textToAnalyse' parameter from the request, 
    processes it using the 'emotion_detector' function.

    Returns: 
        dict: The result of the emotion analysis or an error message of the input is missing
    """
    text_to_analyse = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyse)

    if str(response['dominant_emotion']) is None:
        return "Invalid text! Please try again!"
    return "For the given statement, the system response is 'anger': " + \
        str(response['anger']) + ", 'disgust': " + str(response['disgust']) + \
        ", 'fear': " + str(response['fear']) + ", joy: " + str(response['joy']) + \
        " and sadness: " + str(response['sadness']) + ". The dominant emotion is: " + \
        str(response['dominant emotion']) + "."

@app.route("/")
def render_index_page():
    """
    Renders the html index page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
