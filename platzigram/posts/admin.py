"""Post admin classes.""" 

# Django
from django.contrib import admin

# Models
from .models import Post

# ds: Configuración extra
@admin.register(Post)   # == admin.site.register(Profile, ProfileAdmin)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')  #ds: agrega campos de lectura
    #'user', 'profile', 'title', 'photo', 'created', 'updated'
    list_display = ('id', 'user', 'profile', 'title', 'photo', 'updated')   #Mostrar en columnas de vista previa
    list_display_links = ('id', 'user')   # Hacerlo linkeable para que me lleve al modo edición 
    list_editable = ('title', 'photo')

    search_fields = (       #ds: Agrega buscador
        'user__email', 
        'user__username', 
        'user__first_name', 
        'user__last_name', 
        'profile__phone_number',
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