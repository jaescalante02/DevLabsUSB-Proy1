from django.http import HttpResponse, HttpResponseRedirect
import datetime
import urllib
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render
from django.utils import simplejson
from models import URL

def quiz_guess(request, fact_id):   
   message = []
   if request.is_ajax():
      print 'AJAX'
      #fact = get_object_or_404(Fact, id=fact_id)
      message.append('http://www.w3schools.com/jquery')#fact.type
      #message.append('Es obvio que Marla es una perra!')

   else:
      message.append("You're the lying type, I can just tell.")
   json = simplejson.dumps(message)

   return HttpResponse(json, mimetype='application/json')

#View que despliega la pagina de inicio del sistema
def home(request):
  now= datetime.datetime.now()
  return render (request,'index.html',{'now':now})

