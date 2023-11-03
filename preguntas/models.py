from django.db import models

# Create your models here.
class Pregunta(models.Model):
    
    pregunta= models.CharField(max_length=150)
    
    def __str__(self):
        return self.pregunta

class Respuesta (models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=200)
    es_correcta = models.BooleanField(default=False)
    
    def __str__(self):
        return self.respuesta