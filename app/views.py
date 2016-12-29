from flask import render_template, redirect, flash, request
from bs4 import BeautifulSoup
from app import app
import os, cms

@app.route('/')
def home():
    return render_template('Welcome.html')

@app.route('/getStarted', methods=['GET', 'POST'])
def get_started():
    return render_template('create_page.html')

@app.route('/dbAdd', methods=['GET', 'POST'])
def db_add():
    return render_template('populate_db.html')

@app.route('/generateFile', methods=['GET', 'POST'])
def generate_file():
    file_name = '%s/%s%s' % ('app/templates', request.form['fileName'], '.html')
    charset = request.form['charSet']
    title = request.form['titleAdd']
    cms.populate_file(file_name, unicode(charset), unicode(title))
    return "File created successfully!"

@app.route('/addSections', methods=['GET', 'POST'])
def add_sections():
    from app import db, models
    import re
    sections = request.form['sectionTypes']
    if sections is not None:
        split_sections = re.split('(?<!\d)[,.](?<!d)', sections)
        for section in split_sections:
            s = models.HTML_Sections(name=section)
            db.session.add(s)
        db.session.commit()
    flash('Section types added successfully')
    return render_template('populate_db.html')
