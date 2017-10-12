#-*- coding: utf-8 -*-
from datetime import datetime
from jinja2 import Template
from slugify import slugify

import os
import sys
import csv


class Book(object):
    title = ''
    isbn10 = ''
    isbn13 = ''
    authors = ''
    publisher = ''
    published = ''
    tags = []

    @property
    def tags_as_css_class(self):
        return ' '.join(self.tags)

    @property
    def slug(self):
        return slugify(self.title)


def to_html(**kwargs):
    books = kwargs.get('books')
    tags = kwargs.get('tags')
    now = datetime.now()
    today = datetime.strftime(now, '%Y-%m-%d')
    data = {
        'books': books,
        'total': len(books),
        'last_update': today,
        'tags': tags
    }

    with open('html/_template.html', 'r') as t:
	    source = t.read()
    template = Template(source)
    html = template.render(data)
    with open('index.html', 'w') as f:
        f.write(html)

def sort_by_title(books):
    def get_title(book):
        return book.slug
    return sorted(books, key=get_title)

def get_unique_tags_from(books):
    tags = []
    for b in books:
        for t in b.tags:
            if not t in tags:
                tags.append(t)
    return sorted(tags)

if __name__ == '__main__':
    filename = sys.argv[1]
    books = []
    with open(filename, 'r') as csvfile:
        fieldnames = ['ISBN-10', 'ISBN-13', 'Published', 'Authors', 'Publisher', 'Title', 'Tags']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames, lineterminator='\n', delimiter='|')
        for row in reader:
            book = Book()
            book.title = row.get('Title')
            book.isbn10 = row.get('ISBN-10')
            book.isbn13 = row.get('ISBN-13')
            book.publisher = row.get('Publisher')
            book.published = row.get('Published')
            book.tags = row.get('Tags').split(',')
            book.image = 'images/%s.jpg' % row.get('ISBN-13')
            books.append(book)

    books = sort_by_title(books)
    tags = get_unique_tags_from(books)
    to_html(books=books, tags=tags)
    print('Success')

