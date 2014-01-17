from django.db import models

class URL(models.Model):

  url = models.CharField(max_length=100, primary_key=True)
  puntuacion = models.IntegerField(default=1)
  
  def __unicode__(self):
      return self.url+' '+str(self.puntuacion)
        
