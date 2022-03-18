from pathlib import Path
from django.urls import path
from RestFrameworkApi.views import list_instituciones,create_institucion

urlpatterns = [
    path('institucionesRestFramework/', list_instituciones),
    path('institucionesRestFramework/create/', create_institucion),
    
]
