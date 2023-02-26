from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from myapiapp.serializers import TutorialSerializers
from .models import Tutorial,TutorialCategory,TutorialSeries
from rest_framework import status
# Create your views here.


class TutorialView(APIView):
    serializer_class = TutorialSerializers
    
    def get(self,request,id=None):
        if not id:
            All_Data=Tutorial.objects.all()
            print("data: ", All_Data)
            my_list=[]
            for data in All_Data:
                my_dict={}
                print("my_list: ", my_list)
                my_dict['Id']=data.id
                my_dict['tutorial_content']= data.tutorial_content
                my_dict['tutorial_published']=str(data.tutorial_published)
                my_dict['tutorial_series']=data.tutorial_series.id
                my_dict['tutorial_slug'] = data.tutorial_slug
                my_list.append(my_dict)
            return Response({"message": "response from get", "data": my_list},status=status.HTTP_200_OK)
        else:
            get_data=Tutorial.objects.get(id=id)
            if get_data:
                my_dict = {}
                my_dict['Id']=get_data.id
                my_dict['tutorial_content']= get_data.tutorial_content
                my_dict['tutorial_published']=str(get_data.tutorial_published)
                my_dict['tutorial_series']=get_data.tutorial_series.id
                my_dict['tutorial_slug'] = get_data.tutorial_slug
                return Response({"message":my_dict})
        


    
    def post(self, request, *args, **kwargs):
        data  = request.data
        print(data)
        tutorial_serializer = TutorialSerializers(data=data)
        if tutorial_serializer.is_valid():
            save_data = tutorial_serializer.save()
            print("tuto_data: ", tutorial_serializer.data)
            return Response({"message": tutorial_serializer.data})
        return Response({"message": "not a valid request"}, status=400)
    
    def put(self,request,id=None):
        Tutorial_data = Tutorial.objects.filter(id=id).first()
        tutorial_serializer = TutorialSerializers(Tutorial_data,request.data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return Response ({"message": tutorial_serializer.data})
        return Response(tutorial_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,id=None):
        Tutorial_data = Tutorial.objects.filter(id=id).first()
        tutorial_serializer = TutorialSerializers(Tutorial_data,request.data,partial=True)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return Response ({"message": tutorial_serializer.data})
        return Response(tutorial_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, id=None):
        Tutorial_data = Tutorial.objects.filter(id=id)
        Tutorial_data.delete()
        return Response({"message":"Delete successful"},status=status.HTTP_204_NO_CONTENT)
