# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 00:10:22 2025

@author: HP
"""

from flask import Flask, request

app = Flask(__name__)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    return f"Spotify authorization code received: {code}"

@app.route("/")
def index():
    return "Hello! This is the redirect app."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
