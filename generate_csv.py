from bs4 import BeautifulSoup
from datetime import datetime
from slugify import slugify

import os
import sys
import json
import csv


def to_dict(data):
    result = {
        'Title': '',
        'ISBN-10': '',
        'ISBN-13': '',
        'Authors': None,
        'Edition': '',
        'Binding': '',
        'Publisher': '',
        'Published': None,
        'List Price': '',
        'Tags': []
    }
    for d in data:
        if d[0] == 'Author': d[0] = 'Authors'
        result.update({d[0]: d[1].strip()})

    authors = result.get('Authors') or ''
    a = [authors]
    if ';' in authors:
        a = authors.split('; ')
    result.update({'Authors': a})

    published = result.get('Published')
    if published:
        published_at = datetime.strptime(published, '%B %Y')
        result.update({'Published': datetime.strftime(published_at, '%Y-%m')})

    return result

def parse(content):
    soup = BeautifulSoup(content, 'html.parser')
    div = soup.select_one('div.bookinfo')
    data = [p.get_text().split(':') for p in div.select('p')]
    try:
        title = div.select_one('h2').get_text()
    except:
        title = div.select_one('h1').get_text()
        
    data.append(['Title', title])
    return data

def to_csv(books, out):
    with open(out, 'w') as csvfile:
        fieldnames = ['ISBN-10', 'ISBN-13', 'Published', 'Authors', 'Publisher', 'Title', 'Tags']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator='\n', delimiter='|') #csv.excel_tab.delimiter)
        #writer = csv.writer(csvfile, lineterminator='\n', delimiter='|') #csv.excel_tab.delimiter)
        #writer.writeheader()
        for d in books:
            try:
                writer.writerow({
                    'ISBN-10': d.get('ISBN-10'),
                    'ISBN-13': d.get('ISBN-13'),
                    'Published': d.get('Published'),
                    'Authors': ', '.join(d.get('Authors')).encode("utf-8"),
                    'Publisher': d.get('Publisher'),
                    'Title': d.get('Title'),
                    'Tags': ''
                })
            except Exception as e:
                print '[ERROR] %s: %s - %s' % (d.get('ISBN-13'), d.get('Title'), e)

def to_json(books):
    books_str = json.dumps(books)
    with open('books.json', 'wb') as f:
        f.write(books_str)


if __name__ == '__main__':
    directory = sys.argv[1]
    books = []
    print '###### Starting %s' % directory
    for item in os.listdir(directory):
        if not item.endswith('.html'):
            continue

        with open(os.path.join(directory, item), 'rb') as f:
            content = f.read()
            try:
                data = parse(content)
                book = to_dict(data)
                books.append(book)
                print '%s: %s' % (item.replace('.html', ''), slugify(book.get('Title')))
            except Exception as e:
                print '[ERROR] %s. %s' % (item, e)

    to_csv(books, sys.argv[2])

