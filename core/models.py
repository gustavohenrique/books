from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return u'%s' % self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return u'%s' % self.name


class Book(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateField(blank=True, null=True, verbose_name='Publication')
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    author = models.ForeignKey(Author, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.title

