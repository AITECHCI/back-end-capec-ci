from django.db import models

class HomePage(models.Model):
    presentation = models.TextField()
    mission = models.TextField()
    vision = models.TextField()

class AboutPage(models.Model):
    history = models.TextField()
    team = models.TextField()
    values = models.TextField()

class ResearchTheme(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Research(models.Model):
    themes = models.ManyToManyField(ResearchTheme)
    sponsored_studies = models.TextField()
    research_methods = models.TextField()

class PublicationType(models.Model):
    name = models.CharField(max_length=255)

class Publication(models.Model):
    type = models.ForeignKey(PublicationType, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='publications/')

class Activity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()

class TrainingProgram(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Media(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='media/')
    video = models.FileField(upload_to='media/', null=True, blank=True)

class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()