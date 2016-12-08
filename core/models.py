from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify

import os


class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return u'%s' % self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return u'%s' % self.name

def update_filename(instance, filename):
    path = "covers/"
    format = u'%s.%s' % (slugify(instance.title), filename[-3:len(filename)])
    return os.path.join(path, format)


class Book(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateField(blank=True, null=True, verbose_name='Publication')
    cover = models.ImageField(upload_to=update_filename, blank=True, null=True)
    author = models.ForeignKey(Author, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __unicode__(self):
        return u'%s' % self.title

