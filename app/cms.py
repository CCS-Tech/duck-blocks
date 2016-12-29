from bs4 import BeautifulSoup
import os


def populate_file(html_file, char_set, html_title):
    soup = BeautifulSoup(html_file, "html5lib")
    head_info = soup.head
    charset = soup.new_tag('meta')
    charset.attrs['charset'] = char_set
    http_equiv = soup.new_tag('meta')
    http_equiv.attrs['content'] = 'ie=edge'
    http_equiv.attrs['http-equiv'] = 'x-ua-compatible'
    viewport = soup.new_tag('meta')
    viewport.attrs['content'] = 'width=device-width, initial-scale=1.0'
    viewport.attrs['name'] = 'viewport'
    title = soup.new_tag('title')
    title.append(html_title)
    foundation_css = soup.new_tag('link')
    foundation_css.attrs['href'] = '/static/foundation.min.css'
    foundation_css.attrs['rel'] = 'stylesheet'
    custom_css = soup.new_tag('link')
    custom_css.attrs['href'] = '/static/style.css'
    custom_css.attrs['rel'] = 'stylesheet'
    head_info.append(charset)
    head_info.append(title)
    head_info.append(http_equiv)
    head_info.append(viewport)
    head_info.append(foundation_css)
    head_info.append(custom_css)
    soup.body.clear()
    html = soup.prettify('utf-8')
    with open(html_file, 'wb') as _file:
        _file.write(html)
