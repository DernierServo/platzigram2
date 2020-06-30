"""User admin classes.""" 

# Django
from django.contrib import admin

# Models
from .models import Profile

# ds: Configuración extra
@admin.register(Profile)    # == admin.site.register(Profile, ProfileAdmin)
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')  #ds: agrega campos de lectura
    
    list_display = ('id', 'user', 'phone_number', 'website', 'picture')   #Mostrar en columnas de vista previa
    list_display_links = ('id', 'user')   # Hacerlo linkeable para que me lleve al modo edición 
    list_editable = ('phone_number', 'website', 'picture')

    search_fields = (       #ds: Agrega buscador
        'user__email', 
        'user__username', 
        'user__first_name', 
        'user__last_name', 
        'phone_number'
    )    

    list_filter = (         #ds: Filtro para búsqueda
        'user__is_active',
        'user__is_staff',
        'created', 
        'updated',
    )  

    ordering = ('-created',)

# ds: Configuración del Panel
title = "Proyecto con Django con Platzo"
subtitle = "Panel de Gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
