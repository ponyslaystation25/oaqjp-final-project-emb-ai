from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotion_detector')
def emotion_detection_route():
    text_to_analyse = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyse)

    return "For the given statement, the system response is 'anger': " + str(response['anger']) + ", 'disgust': " + str(response['disgust']) + ", 'fear': " + str(response['fear']) + ", joy: " + str(response['joy']) + " and sadness: " + str(response['sadness']) + ". The dominant emotion is: " + str(response['dominant emotion']) + "."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
