'''
    met-image-url-scraper.py
'''
import sys
import re
import urllib.request

def image_url(page_url):
    ''' Given the URL for one of the Met's single-artwork pages, retrieve
        that page, extract the artwork's image url, and return that url.
        If this fails, return an empty string. '''
    data_from_server = urllib.request.urlopen(page_url).read()
    string_from_server = data_from_server.decode('utf-8')
    match = re.search(r'<img id="artwork__image".*src="([^"]*)"', string_from_server)
    if match:
        return match.group(1)
    return ''

print(image_url('https://www.metmuseum.org/art/collection/search/383684'))