from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_delete
from django.dispatch import receiver

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
    return u'%s.%s' % (slugify(instance.title), filename[-3:len(filename)])

class Book(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=255, blank=True, null=True)
    pub_date = models.DateField(blank=True, null=True, verbose_name='Publication')
    cover = models.ImageField(upload_to=update_filename, blank=True, null=True)
    author = models.ForeignKey(Author, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __unicode__(self):
        return u'%s' % self.title

@receiver(post_delete, sender=Book)
def delete_files(sender, **kwargs):
    instance = kwargs.get('instance')
    if instance.cover:
        os.remove(instance.cover.path)

