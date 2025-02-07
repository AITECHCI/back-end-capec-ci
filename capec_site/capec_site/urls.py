"""
Configuration des URL pour le projet capec_site.

La liste `urlpatterns` associe les URLs aux vues. Pour plus d'informations, veuillez consulter :
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Exemples :
Vues fonctionnelles
    1. Ajoutez une importation :  from my_app import views
    2. Ajoutez une URL à urlpatterns :  path('', views.home, name='home')
Vues basées sur des classes
    1. Ajoutez une importation :  from other_app.views import Home
    2. Ajoutez une URL à urlpatterns :  path('', Home.as_view(), name='home')
Inclure un autre URLconf
    1. Importez la fonction include() : from django.urls import include, path
    2. Ajoutez une URL à urlpatterns :  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL de l'interface d'administration
    path('', include('content.urls')),  # Route pour l'application principale
]