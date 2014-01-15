from django.http import HttpResponse, HttpResponseRedirect
import datetime
import urllib
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render
from django.utils import simplejson
from models import URL
from django.db.models import Sum
import random

def quiz_guess(request, fact_id):   
   message = []
   if request.is_ajax():
      print 'AJAX'
      #fact = get_object_or_404(Fact, id=fact_id)
      if(int(fact_id)==2):
          message.append('T')#fact.type
          message.append('Viste clase con ella cierto?')
	  #v1 = Votacion(1,'http://www.paginadejuan.com',0)
          #Votacion.save(v1)
      else:
          #v1 = Votacion(4,'http://www.paginadePatrick.com',0)
          #Votacion.save(v1)

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

#Funcion para calcular la probabilidad
def recta_prob():
    res = URL.objects.all()
    suma = res.aggregate(Sum('puntuacion'))['puntuacion__sum']
    listaUrls = res.values_list()
    
    # Asignar a cada elemento su probabilidad
    j = 0.0
    recta = []
    for i in listaUrls:
        recta.append((i[0],j,j + i[1] / float(suma)))
        j += i[1] / float(suma)
        
    return recta

# Funcion que busca en la recta el elemento correspondiente
def buscarEnRecta(recta,n):
    for i in recta:
        if i[1]<=n and n<=i[2]:
            return i[0]

# Funcion que obtiene una pagina aleatoria
def obtenerPagAleatoria():
    n = random.uniform(0.0,1.0)
    recta = recta_prob()
    url = buscarEnRecta(recta,n)
    print url

