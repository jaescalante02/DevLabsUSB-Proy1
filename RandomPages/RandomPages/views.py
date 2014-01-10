from django.http import HttpResponse, HttpResponseRedirect
import datetime
import urllib
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render
from django.utils import simplejson
from models import Votacion

def quiz_guess(request, fact_id):   
   message = []
   if request.is_ajax():
      print 'AJAX'
      #fact = get_object_or_404(Fact, id=fact_id)
      if(int(fact_id)==2):
          message.append('T')#fact.type
          message.append('Viste clase con ella cierto?')
	  v1 = Votacion(1,'http://www.paginadejuan.com',0)
          Votacion.save(v1)
      else:
          v1 = Votacion(4,'http://www.paginadePatrick.com',0)
          Votacion.save(v1)

          message.append('F')#fact.type
          message.append('Es obvio que Marla es una perra!')

   else:
      message.append("You're the lying type, I can just tell.")
   json = simplejson.dumps(message)
   return HttpResponse(json, mimetype='application/json')

#View que despliega la pagina de inicio del sistema
def home(request):
  now= datetime.datetime.now()
  return render (request,'index.html',{'now':now})
