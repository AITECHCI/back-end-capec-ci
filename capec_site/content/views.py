from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import MyModelForm  # Remplacez par votre formulaire
from .models import HomePage, AboutPage, Research, Publication, Activity, TrainingProgram, Media, Contact, FAQ

def create_object(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Objet créé avec succès !')
            return redirect(reverse('admin:content_mymodel_changelist'))  # Redirige vers la liste des objets dans l'admin
    else:
        form = MyModelForm()
    
    return render(request, 'admin/content/mymodel/create.html', {'form': form})

def home(request):
    home_page = HomePage.objects.first()
    return render(request, 'home.html', {'home_page': home_page})

def about(request):
    about_page = AboutPage.objects.first()
    return render(request, 'about.html', {'about_page': about_page})

def research(request):
    research = Research.objects.first()
    return render(request, 'research.html', {'research': research})

def publications(request):
    publications = Publication.objects.all()
    return render(request, 'publications.html', {'publications': publications})

def activities(request):
    activities = Activity.objects.all()
    return render(request, 'activities.html', {'activities': activities})

def training(request):
    programs = TrainingProgram.objects.all()
    return render(request, 'training.html', {'programs': programs})

def media(request):
    media_items = Media.objects.all()
    return render(request, 'media.html', {'media_items': media_items})

def contact(request):
    contact_info = Contact.objects.first()
    return render(request, 'contact.html', {'contact_info': contact_info})

def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})