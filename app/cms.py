from bs4 import BeautifulSoup
from flask import request
import os

class content_managment:

    def __init__(self, html_file):
        self.html_file = html_file

    def generate_file(self):
        save_path = 'templates'
        full_name = os.path.join(save_path, self.html_file)
        soup = BeautifulSoup('''\
        <!DOCTYPE html>
        <html><head></head><body></body</html>
        ''', "html5lib")
        with open(full_name, 'w+') as file_:
            file_.write(soup.prettify('utf-8'))
        return 'File created successfully!'

    def populate_file(self, html_file):
            chars = request.form['charSet']
            title = request.form['titleAdd']
            open('templates' + self.html_file, 'r+')
            soup = BeautifulSoup(html_doc, 'html5lib')
            page_head = soup.new_tag('head')
            head_info = page_head.find_next()

            return 'File created successfully!'
