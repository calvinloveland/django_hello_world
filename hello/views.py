from django.http import HttpResponse
from models import Visitors
import datetime

def index(request):
    #I messed up the database, no idea how to fix it, created a ton of visitors 
    #I added this messed_up_the_database value and now there is only one
    #visitor with the messed_up_the_database = 1
    visitor_count = Visitors.objects.get_or_create(messed_up_the_database = 1) 
    visitor_count[0].visit_count +=1
    visitor_count[0].save()
    return HttpResponse("Hello, world. The time at the server is: " + str(datetime.datetime.now().time())+ "!" +
    "\n You are the: " +  str(visitor_count[0].visit_count) + "th visitor")