from django.contrib import admin
from .models import universidad,programa_academicos,curso,comentario,curso_programa
# Register your models here.

admin.site.register(universidad)
admin.site.register(programa_academicos)
admin.site.register(curso)
admin.site.register(comentario)
admin.site.register(curso_programa)
