from flask import Flask, render_template, send_file
import random
from gtts import gTTS
import os
import uuid  # To generate unique filenames

app = Flask(__name__)

# Define a directory to store temporary audio files
audio_dir = 'audio/'

# Ensure the audio directory exists
os.makedirs(audio_dir, exist_ok=True)

# Load jokes from a file into a list with the correct encoding (e.g., 'utf-8')
with open('jokes.txt', 'r', encoding='utf-8', errors='replace') as file:
    jokes = file.read().splitlines()

@app.route('/')
def index():
    # Select a random joke
    random_joke = random.choice(jokes)
    print(random_joke)
    # Generate a unique audio file for the joke
    audio_filename = 'joke.mp3'
    audio_file_path = os.path.join(audio_dir, audio_filename)

    tts = gTTS(text=random_joke, lang='en')
    tts.save(audio_file_path)

    return render_template('index.html', audio_filename=audio_filename,random_joke=random_joke)

@app.route('/audio/<audio_filename>')
def serve_audio(audio_filename):
    audio_file_path = os.path.join(audio_dir, audio_filename)
    return send_file(audio_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
