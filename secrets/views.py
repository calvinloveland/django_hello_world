from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Note
from .models import id_generator


class IndexView(generic.TemplateView):
    template_name = 'secrets/index.html'


class CreateView(generic.CreateView):
    model = Note
    fields = ['note_text']
    
    
class CreatedView(generic.TemplateView):
    template_name = 'secrets/created.html'
    
    
def view_note(request, given_note_id):
    template = 'secrets/view_note.html'
    note = get_object_or_404(Note,note_id = given_note_id)
    return render(request, template, {'note': note})
