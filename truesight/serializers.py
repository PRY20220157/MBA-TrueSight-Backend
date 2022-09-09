from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from .models import *

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['countryId','country']

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ['userTypeId','userType']

class StatExportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatExportType
        fields = ['statExportTypeId','statExportType']
        
class PredictionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionType
        fields = ['predictionTypeId','predictionType']

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['universityId','university','countryId','university_email']

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['userInfoId','userId','countryId','universityId','firstName','lastName','creationDate','updatedDate']

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ['predictionId','userId','gmatScore','gpaScore','workExp','appType','gradGpaScore','creationDate','massivePredictionId','predictionTypeId']

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['userId','userTypeId','email','password']