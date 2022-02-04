from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/")
def title():
    return "<h1>A big title of machine AAA</h1>"