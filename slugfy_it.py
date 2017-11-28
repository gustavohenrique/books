#!/usr/bin/env python
from slugify import slugify
import sys

if __name__ == '__main__':
    print(slugify(sys.argv[1]))
