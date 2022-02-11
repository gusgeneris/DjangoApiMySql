from django.shortcuts import render
from django.views import View
from .models import *
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator #se importa el decorador
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

class EmpresaView(View):
    @method_decorator(csrf_exempt) #cada ves que se envie se ejecuta el decorador con el cual el parametro csrf salta la restriccion
    def dispatch(self, request, *args, **kwargs):# Metodo que se ejecuta cada ves que se envie una peticion 
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request,id=0):
        if id>0:
            empresa=list(Empresa.objects.filter(id=id).values())
            if len(empresa) > 0:
                datos={'mensaje':"Correcto",'empresa':empresa} # Buscar por id
            else:
                datos={'mensaje':"Sin datos"}
            return JsonResponse(datos)
        else:
            empresas = list(Empresa.objects.values())# Por medio de un casting se transforman los objetos extraidos del modelo a una lista.
            if len(empresas) > 0:
                datos={'mensaje':"Correcto",'empresas':empresas}
            else:
                datos={'mensaje':"Sin datos"}
            return JsonResponse(datos)
    
    
    def post(self,request):
        #print(request.body)
        #se debe convertir los datos enviados por el request en un diccionario que python pueda manipular.
        jd = json.loads(request.body)
        
        #print(jd)
        Empresa.objects.create(
            nombre = jd['nombre'],
            url = jd['url'],
            createdDate = jd['createdDate']
        )
        datos={'mensaje':"Correcto"}
        return JsonResponse(datos)
    
    def put(self, request,id):
        jd=json.loads(request.body)
        empresa=list(Empresa.objects.filter(id=id).values())
        
        if len(empresa) > 0:
            empresa=Empresa.objects.get(id=id)
            empresa.nombre = jd['nombre']
            empresa.url = jd['url']
            empresa.createdDate = jd['createdDate']
            empresa.save()
            datos={'mensaje':"Correcto"}
        else:
            datos={'mensaje':"Sin datos"}
        return JsonResponse(datos)
         
    
    def delete(self,request,id):
        empresa=list(Empresa.objects.filter(id=id).values())
        if len(empresa) > 0:
            Empresa.objects.filter(id=id).delete()
            datos={'mensaje':"Correcto"}
        else:
            datos={'mensaje':"Sin datos"}
        return JsonResponse(datos)