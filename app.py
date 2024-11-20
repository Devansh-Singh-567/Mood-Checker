from flask import Flask, request, jsonify, send_file
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

@app.route('/')
def index():
    # Serve the index.html file from the root directory
    return send_file('index.html')

@app.route('/analyze_mood', methods=['POST'])
def analyze_mood():
    user_input = request.form['user_input']
    
    # Analyze sentiment
    sentiment = analyzer.polarity_scores(user_input)
    score = sentiment['compound']
    
    # Determine mood and song link based on sentiment score
    if score <= -0.5:
        mood = 'sad'
        song_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Example hype song
    elif score >= 0.5:
        mood = 'happy'
        song_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Example cheerful song
    else:
        mood = 'neutral'
        song_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Example cheerful song
    
    return jsonify({"mood": mood, "song_link": song_link})

if __name__ == '__main__':
    app.run(debug=True)
