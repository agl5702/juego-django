from django.contrib import admin
from .models import Respuesta, Pregunta
# Register your models here.

class RespuestaAdmin(admin.ModelAdmin):
    list_display= ['respuesta']
    
class PreguntaAdmin(admin.ModelAdmin):
    list_display= ['pregunta']
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta, RespuestaAdmin)
