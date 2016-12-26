from bs4 import BeautifulSoup
import os


def populate_file(html_file, char_set, html_title):
    soup = BeautifulSoup(html_file, "html5lib")
    head_info = soup.head
    charset = soup.new_tag('meta')
    charset.attrs['charset'] = char_set
    title = soup.new_tag('title')
    title.append(html_title)
    head_info.append(charset)
    head_info.append(title)
    soup.body.clear()
    html = soup.prettify('utf-8')
    with open(html_file, 'wb') as _file:
        _file.write(html)
