from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import Http404
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Note
from .models import Viewer

import datetime
from ipware.ip import get_ip

class IndexView(generic.TemplateView):
    template_name = 'secrets/index.html'


class CreateView(generic.CreateView):
    model = Note
    fields = ['note_text','password']
    
class CreatedView(generic.TemplateView):
    template_name = 'secrets/created.html'
  
class AboutView(generic.TemplateView):
    template_name = 'secrets/about.html'  
    
def view_note(request, given_note_id):
    template = 'secrets/view_note.html'
    note = get_object_or_404(Note,note_id = given_note_id)
    viewer = note.viewer;
    return render(request, template, {'viewer': viewer })
    
def get_note(request):
    note = get_object_or_404(Note,note_id = request.POST.get('id',''))
    viewer = note.viewer
    if viewer.expiry < timezone.now():
        viewer.delete()
        return HttpResponse('<h1>Note has expired</h1>')
    if viewer.viewed:
        return HttpResponse('<h1>Note destroyed</h1>')
    if note.password != '' and request.POST.get('password','') != note.password:
        return HttpResponse('<h1>Incorrect password</h1>')
    viewer.ip = get_ip(request)
    viewer.viewed = True;
    viewer.viewed_time = timezone.now()
    viewer.save();
    template = 'secrets/note_response.html'
    return render(request,template,{'note':note})

def get_stats(request,given_note_id):
    template = 'secrets/view_stats.html'
    note = get_object_or_404(Note,note_id = given_note_id)
    viewer = note.viewer;
    return render(request, template, {'viewer': viewer })

