"""Server for Emotion Detection Web Application."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(
    __name__,
    template_folder='oaqjp-final-project-emb-ai/templates',
    static_folder='oaqjp-final-project-emb-ai/static'
)


@app.route('/')
def home():
    """
    Render the homepage of the Emotion Detection app.

    Returns:
        str: Rendered HTML template for homepage.
    """
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET'])
def emotion_detection():
    """
    Handle emotion detection request from the user.

    Returns:
        str: Text describing the detected emotions or an error message.
    """
    text_to_analyse = request.args.get('textToAnalyze')

    if not text_to_analyse:
        return "Error: No text provided."

    result = emotion_detector(text_to_analyse)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response


if __name__ == '__main__':
    app.run(debug=True)
