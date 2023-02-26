
from .models import Tutorial,TutorialCategory,TutorialSeries
from rest_framework import serializers





class TutorialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields='__all__'

class TutorialCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = TutorialCategory
        fields='__all__'

class TutorialSeriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = TutorialSeries
        fields='__all__'