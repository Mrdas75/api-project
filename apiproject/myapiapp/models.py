from django.db import models

# Create your models here.


class TutorialCategory(models.Model):

    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1)

   

class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)

    tutorial_category = models.ForeignKey(TutorialCategory, default=1, on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

   
    
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published')
    tutorial_series = models.ForeignKey(TutorialSeries, default=1, on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=200, default=1)
   