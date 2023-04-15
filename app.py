from transformers import pipeline
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
transcriber = pipeline(model="openai/whisper-small")

@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/transcribe')
def transcribe():
    res=transcriber('cardiacArrest.mp3')
    print(res)
    return res


