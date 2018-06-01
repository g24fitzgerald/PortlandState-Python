#http://api.icndb.com/jokes/random

from flask import Flask, render_template, jsonify, request
import requests
import json
#if another script imoirts this file, the name will be the name of the file (here it's main bc main.py)
app = Flask(__name__) #name reveals name of current file. ensures correct file is running

#make decorator to declare where route points to
@app.route('/')
def index():
    url = 'http://api.icndb.com/jokes/random'
    resp = requests.get(url)
    return render_template('index.html', joke=eval(resp.text)["value"]["joke"] )

@app.route('/get_fact')
#code to return new chuck norris fact
def get_fact():
    url = 'http://api.icndb.com/jokes/random'
    resp = requests.get(url)
    return resp.text

if __name__ == '__main__': #says if app
    app.run(debug = True) #provide default parameter
