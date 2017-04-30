from __future__ import unicode_literals

from django.db import models
import string
import random
import datetime

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
    

class Note(models.Model):
    note_text = models.TextField(max_length = 1000)
    note_id = models.CharField(max_length = 10,default = id_generator(), unique = True)
    password = models.CharField(max_length = 64,default = '',blank = True)
    
    
    def save(self, *args, **kwargs):
        while len(Note.objects.filter(note_id = self.note_id)) != 0:
            self.note_id = id_generator()
        super(Note,self).save(*args, **kwargs)
        if not hasattr(self,'Viewer'):
            viewer = Viewer(note = self)
            viewer.save()
    
    def get_absolute_url(self):
        return '/secrets/created/' + self.note_id
    
class Viewer(models.Model):
    note = models.OneToOneField(Note,on_delete = models.CASCADE)
    ip = models.GenericIPAddressField(default = '198.2.2.2')
    expiry = models.DateTimeField(default = datetime.datetime.now() + datetime.timedelta(days = 7))
    viewed = models.BooleanField(default = False)
    viewed_time = models.DateTimeField(default = datetime.datetime.now())
    