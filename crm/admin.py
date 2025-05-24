from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.utils.html import format_html
from django.contrib.staticfiles.storage import staticfiles_storage
from .models import Cliente, Servicio, Cita

class MyAdminSite(AdminSite):
    site_header = "CRM Personalizado"
    site_title = "Administración del CRM"
    index_title = "Panel de Administración"

    def each_context(self, request):
        context = super().each_context(request)
        context['custom_admin_css'] = format_html(
            '<link rel="stylesheet" type="text/css" href="{}">',
            staticfiles_storage.url('crm/admin.css')
        )
        return context

# Usa tu clase personalizada
admin.site.__class__ = MyAdminSite

# Registro de modelos
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ('cedula', 'nombre')
    list_display = ('nombre', 'email', 'telefono', 'cedula', 'ciudad')

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = (
        'cliente',
        'cliente_cedula',
        'mostrar_servicios',
        'valor_total',
        'fecha',
        'hora',
        'observaciones',
    )
    list_filter = ('fecha',)
    autocomplete_fields = ['cliente']

    def cliente_cedula(self, obj):
        return obj.cliente.cedula
    cliente_cedula.short_description = 'Cédula Cliente'

    def mostrar_servicios(self, obj):
        return ", ".join([s.nombre for s in obj.servicios.all()])
    mostrar_servicios.short_description = 'Servicios'

    def valor_total(self, obj):
        total = sum(s.precio for s in obj.servicios.all())
        return "${:,.0f}".format(total).replace(",", ".")
    valor_total.short_description = 'Valor Total'

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_formateado')

    def precio_formateado(self, obj):
        return "${:,.0f}".format(obj.precio).replace(",", ".")
    precio_formateado.short_description = 'Precio'

