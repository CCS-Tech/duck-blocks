from flask import render_template, redirect, request
from bs4 import BeautifulSoup
from app import app
import os, cms

@app.route('/')
def home():
    return render_template('Welcome.html')

@app.route('/getStarted', methods=['GET', 'POST'])
def get_started():
    return render_template('create_page.html')

@app.route('/generateFile', methods=['GET', 'POST'])
def generate_file():
    file_name = '%s/%s%s' % ('app/templates', request.form['fileName'], '.html')
    charset = request.form['charSet']
    title = request.form['titleAdd']
    cms.populate_file(file_name, unicode(charset), unicode(title))
    return "File created successfully!"
