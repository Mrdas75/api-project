from django.contrib import admin
from myapiapp import models

# Register your models here.
admin.site.register(models.Tutorial)
admin.site.register( models.TutorialCategory)
admin.site.register(models.TutorialSeries)
