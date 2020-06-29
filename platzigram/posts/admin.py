from django.contrib import admin
from .models import User

# ds: Configuración extra
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')  #ds: agrega campos de lectura
    search_fields = ('first_name', 'last_name')    #ds: Agrega buscador
    list_filter = ('is_admin',)  #Filtro para búsqueda
    list_display = ('first_name', 'last_name', 'email')   #Mostrar en columnas de vista previa
    ordering = ('-created',)

# Register your models here.
admin.site.register(User, UserAdmin)

# ds: Configuración del Panel
title = "Proyecto con Django con Platzo"
subtitle = "Panel de Gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
