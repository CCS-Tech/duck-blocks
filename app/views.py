from flask import render_template, redirect, request
from app import app

@app.route('/')
def home():
    return render_template('Welcome.html')

@app.route('/getStarted', methods=['GET', 'POST'])
def get_started():
    return render_template('create_page.html')
