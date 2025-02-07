from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Vue principale
    path('about/', views.about, name='about'),  # Page À propos
    path('research/', views.research, name='research'),  # Page Recherche
    path('publications/', views.publications, name='publications'),  # Page Publications
    path('activities/', views.activities, name='activities'),  # Page Activités
    path('training/', views.training, name='training'),  # Page Formation
    path('media/', views.media, name='media'),  # Page Médias
    path('contact/', views.contact, name='contact'),  # Page Contact
    path('faq/', views.faq, name='faq'),  # Page FAQ
]