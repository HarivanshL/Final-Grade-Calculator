from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    final_grade = None
    final_gpa = None