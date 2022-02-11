from pathlib import Path
from django.urls import path
from .views import EmpresaView

urlpatterns = [
    path('empresas/',EmpresaView.as_view(), name='empresas_list'),
    
    path('empresas/<int:id>',EmpresaView.as_view(), name='empresas_proces')
]

