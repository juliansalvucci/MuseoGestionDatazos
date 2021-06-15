from django.contrib import admin
from app.models import *

# Traer clases definidas en el modelo.
admin.site.register(Tecnica)
admin.site.register(Estilo)
admin.site.register(TipoRestauracion)
admin.site.register(Especialidad)
admin.site.register(Restaurador)
admin.site.register(Restauracion)
admin.site.register(Artista)
admin.site.register(Obra)
admin.site.register(RestauradorEspecialidad)


class RestauracionInline(admin.TabularInline):
    model = Restauracion
    extra = 0
'''
@admin.register(Restauracion)
class RestauracionAdmin(admin.ModelAdmin):
    inlines = [
        RestauracionInline,
    ]
    list_display = (
        'precio',
    )
    ordering = ['precio']  # -nombre escendente, nombre ascendente
    search_fields = ['precio']
    list_filter = (
        'precios',  #que filtre por precio
    )
'''

# Register your models here.
