from django.contrib import admin
from django.urls import path, reverse
from django.utils.html import format_html
from django.shortcuts import redirect
from .models import HomePage, AboutPage, ResearchTheme, Research, PublicationType, Publication, Activity, TrainingProgram, Media, Contact, FAQ, MyModel
from .views import create_object  # Importez la vue personnalisée

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Remplacez par les champs de votre modèle

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('create/', self.admin_site.admin_view(create_object), name='content_mymodel_create'),
        ]
        return custom_urls + urls

    def add_view(self, request, form_url='', extra_context=None):
        # Redirige vers la vue personnalisée pour la création
        return redirect(reverse('admin:content_mymodel_create'))

    def changelist_view(self, request, extra_context=None):
        # Ajoute un bouton "Créer un nouvel objet" dans la liste des objets
        extra_context = extra_context or {}
        extra_context['custom_button'] = format_html(
            '<a href="{}" class="button">Créer un nouvel objet</a>',
            reverse('admin:content_mymodel_create')
        )
        return super().changelist_view(request, extra_context=extra_context)

# Enregistrement des autres modèles
admin.site.register(HomePage)
admin.site.register(AboutPage)
admin.site.register(ResearchTheme)
admin.site.register(Research)
admin.site.register(PublicationType)
admin.site.register(Publication)
admin.site.register(Activity)
admin.site.register(TrainingProgram)
admin.site.register(Media)
admin.site.register(Contact)
admin.site.register(FAQ)