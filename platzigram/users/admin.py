from django.contrib import admin

from .models import Profile

# ds: Configuración extra
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')  #ds: agrega campos de lectura
    search_fields = ('department',)    #ds: Agrega buscador
    #list_filter = ('is_admin',)  #Filtro para búsqueda
    list_display = ('department', 'website', 'phone_number')   #Mostrar en columnas de vista previa
    ordering = ('-created',)

# Register your models here.
admin.site.register(Profile, ProfileAdmin)

# ds: Configuración del Panel
title = "Proyecto con Django con Platzo"
subtitle = "Panel de Gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
