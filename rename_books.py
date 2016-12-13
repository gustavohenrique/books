import os
import sys

from slugify import slugify

if __name__ == '__main__':
    directory = sys.argv[1]
    books = []
    for item in os.listdir(directory):
        new_name = slugify(item)
        print '%s ... %s' % (item, new_name)
        os.rename(item, new_name)

