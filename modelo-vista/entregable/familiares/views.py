from django.shortcuts import render, HttpResponse
from familiares.models import Familia
# Create your views here.


def datos_familia(request):
    padre = Familia(
        nombre = 'Antonio',
        apellido = 'Garay',
        fecha_nacimiento = '02/05/1943',
        Email_usuario= 'antonio@antonio.com',
        Edad= '79',
        Conexion = 'Padre',
        )
    padre.save()
    
    madre = Familia(
        nombre= 'Maria Teresita',
        apellido= 'Carrasco',
        fecha_nacimiento= '29/09/1948',
        Email_usuario= 'maria@maria.com',
        Edad= '74',
        Conexion = 'Madre'
        )
    madre.save()
    
    hermana = Familia(
        nombre= 'Yudit',
        apellido= 'Garay',
        fecha_nacimiento= '19/11/1972' ,
        Email_usuario= 'yudit@yudit.com',
        Edad= '49',
        Conexion = 'Hermana'
        )
    hermana.save()
    
    
    
    
    


def datos(request):
    
    articulo = Familia.objects.order_by('id')[:3]
    
    return render(request, 'familia.html', {
        'articulos' : articulo
    })

    