from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ClienteForm, ServicioForm, CitaForm
from .models import Cliente, Servicio, Cita

def inicio(request):
    return render(request, 'inicio.html')

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cedula = form.cleaned_data['cedula']
            if Cliente.objects.filter(cedula=cedula).exists():
                form.add_error('cedula', 'Ya existe un cliente con esta cédula.')
            else:
                form.save()
                return redirect('inicio')
    else:
        form = ClienteForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Registrar Cliente'})

def registrar_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ServicioForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Registrar Servicio'})

def registrar_cita(request):
    servicios = Servicio.objects.all()
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            cita = form.save()
            form.save_m2m()  # para guardar relaciones many-to-many
            return redirect('inicio')
    else:
        form = CitaForm()
    return render(request, 'registrar_cita.html', {
        'form': form,
        'servicios': servicios,
        'titulo': 'Registrar Cita'
    })

def buscar_cliente(request):
    cedula = request.GET.get('cedula')
    try:
        cliente = Cliente.objects.get(cedula=cedula)
        return JsonResponse({'nombre': cliente.nombre})
    except Cliente.DoesNotExist:
        return JsonResponse({'error': 'Cliente no encontrado'}, status=404)
