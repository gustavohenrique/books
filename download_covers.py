from bs4 import BeautifulSoup

import urllib.request
import os
import sys
import shutil

def parse(content):
    soup = BeautifulSoup(content, 'html.parser')
    img = soup.select_one('img')
    return {'url': img.get('src')}


if __name__ == '__main__':
    directory = sys.argv[1]
    books = []
    print('###### Starting %s' % directory)
    for item in os.listdir(directory):
        print('- %s' % item)
        if not item.endswith('.html'):
            continue

        with open(os.path.join(directory, item), 'rb') as f:
            content = f.read()
            data = parse(content)
            url = data.get('url')
            filename = '%s%s' % (item[0:len(item) - 4], url[-3:len(url)])
            print('%s %s' % (filename, url))
            dest = os.path.join(sys.argv[2], filename)
            with urllib.request.urlopen(url) as response, open(dest, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
            # urllib.request.urlretrieve(url, os.path.join(sys.argv[2], filename))

