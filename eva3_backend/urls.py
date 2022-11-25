"""eva3_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from administracion import views as administracion
from online import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', administracion.landing_page),
    path('login/', views.login_page),
    path('administracion/', views.renderAdmin),
    path('signin/', views.ingresar),
    path('agregarConsultas/', views.agregarConsulta),
    path('usuarios/', views.renderCliente),
    path('modificarConsultas/<int:id>', views.modificarConsulta),
    path('eliminarConsulta/<int:id>', views.quitarConsulta),
    path('generarRespuesta/<int:id>', views.generarRespuesta),
    path('addanswer/<int:id>', views.guardarRespuesta)
]
