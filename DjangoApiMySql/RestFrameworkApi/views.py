from django.shortcuts import render
from .models import Instituciones
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import (InstitucionSerializer,
                         CreateInstitucionSerializer)

# Create your views here.

@api_view(['GET'])
def list_instituciones(request):
    """Lista todas las Instituciones"""
    instituciones = Instituciones.objects.all()
    serializer = InstitucionSerializer(instituciones, many=True)
    """
    data=[]
    for institucion in instituciones:
        data.append({
           'nombre':institucion.nombre,
            'url': institucion.url, 
        ES SUPLANTADO POR EL SERIALIZER
        
        serializer = InstitucionSerializer(institucion)
        data.append(serializer.data)"""
    data = serializer.data   
    return Response(data)

@api_view(['POST'])
def create_institucion(request):
    """Crea una institucion"""
    
    """ nombre = request.data['nombre']
    url = request.data['url']
    
    institucion = Instituciones.objects.create(nombre=nombre,url=url)
    
    data = {
        'nombre':institucion.nombre,
        'url': institucion.url,
    }
    """
    serializer = CreateInstitucionSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.data
    return Response(data)
    