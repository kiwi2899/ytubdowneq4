#https://www.youtube.com/watch?v=JDcvtKsSfxg
from flask import Flask, render_template, request, Response, redirect, send_file, jsonify
import os
from os import remove
import pafy
import moviepy.editor as mp

app = Flask(__name__)
server = app.server

path = os.getcwd() + '..\\Downloads\\'

@app.route('/')
def route():
    return render_template("index.html")

@app.route('/envia', methods=['GET', 'POST'])
def envia():
    if request.method == 'POST':
        url = request.form.get('url')
        video = pafy.new(url)
        best = video.getbest(preftype="mp4")
        best.download(path)
        p = path + video.title + ".mp4"
    return send_file(p, as_attachment=True)

@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        url = request.form.get('url')
        video = pafy.new(url)
        return render_template('index.html', title=video.title,
                               durat=video.duration, author=video.author,
                               yid=video.thumb, views=video.viewcount, category=video.category)

@app.route('/envia2', methods=['GET', 'POST'])
def envia2():
    if request.method == 'POST':
        url = request.form.get('url')
        video = pafy.new(url)
        best = video.getbest(preftype="mp4")
        best.download(path)
        name = path + video.title + ".mp4"
        clip = mp.VideoFileClip(name)
        clip.audio.write_audiofile(path + video.title + ".mp3")
        p = path + video.title + ".mp3"
    return send_file(p, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
