from __future__ import unicode_literals

from django.db import models
import string
import random

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
    

class Note(models.Model):
    note_text = models.CharField(max_length = 1000)
    note_id = models.CharField(max_length = 10,default = id_generator())
    
    
    def get_absolute_url(self):
        return '/secrets/created/' + self.note_id
    
class Viewer(models.Model):
    note = models.ForeignKey(Note,on_delete = models.CASCADE)