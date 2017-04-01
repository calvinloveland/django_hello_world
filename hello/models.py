from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Visitors(models.Model):
    messed_up_the_database = models.IntegerField()
    visit_count = models.IntegerField(default=0)