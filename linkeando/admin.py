from django.contrib import admin
from models import Enlace, Categoria, Agregador


class EnlaceAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'enlace', 'categoria',
                    'imagen_voto', 'es_popular')
    list_filter = ('categoria', 'usuario')
    search_fields = ('categoria__titulo',)
    list_editable = ('enlace', 'categoria')
    raw_id_fields = ('categoria', 'usuario',)

    def imagen_voto(self, obj):
        url = obj.mis_votos_en_imagen_rosada()
        tag = '<img src = "%s">' % url
        return tag
    imagen_voto.allow_tags = True
    imagen_voto.admin_order_field = 'votos'


class EnlaceInLine(admin.StackedInline):
    model = Enlace
    extra = 1
    raw_id_fields = ("usuario",)


class CategotiaAdmin(admin.ModelAdmin):
    inlines = [EnlaceInLine]


class AgregadorAdmin(admin.ModelAdmin):
    filter_horizontal = ('enlace',)

admin.site.register(Agregador, AgregadorAdmin)
admin.site.register(Categoria, CategotiaAdmin)
admin.site.register(Enlace, EnlaceAdmin)
