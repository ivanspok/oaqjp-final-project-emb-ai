"""
Main server for final project
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detection():
    """
    Emotion Detecton route
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is not None:
        output_text =''
        for key, value in response.items():
            if key != 'dominant_emotion':
                output_text += f'{key}:{value:.4f} '
        output = f"For the given statement, the  system response is {output_text}. \
        The dominant emotion is {response['dominant_emotion']}"
        return output
    return "Invalid text! Please try again!"

@app.route("/")
def render_index_page():
    """
    Render index.html page
    """
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
