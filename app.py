from flask import Flask, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def home():
    return open("index.html").read()

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    
    ydl_opts = {
    'format': 'best',
    'merge_output_format': 'mp4',
    'outtmpl': 'downloads/%(id)s.%(ext)s',
    'restrictfilenames': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    for file in os.listdir():
        if file.startswith("video"):
            return send_file(file, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
