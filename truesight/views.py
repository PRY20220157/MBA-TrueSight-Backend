
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



#Countries
@api_view(['GET','POST'])
def countryList(request, format=None):

    if request.method == 'GET':
    #get all countries, serialize and return json
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def countryDetail(request, countryId, format=None):

    try:
        country = Country.objects.get(countryId=countryId)
    except Country.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    elif request.method =='PUT':
        serializer = CountrySerializer(country,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#UserType
@api_view(['GET','POST'])
def userTypeList(request, format=None):
    if request.method == 'GET':
        userTypes = UserType.objects.all()
        serializer = UserTypeSerializer(userTypes, many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=UserTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    
@api_view(['GET','PUT','DELETE'])
def userTypeDetail(request,userTypeId,format=None):
    
    try:
        userType = UserType.objects.get(userTypeId=userTypeId)
    except UserType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserTypeSerializer(userType)
        return Response(serializer.data)

    elif request.method =='PUT':
        serializer = UserTypeSerializer(userType,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        userType.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#StatExportType
@api_view(['GET','POST'])
def statExportTypeList(request, format=None):
    if request.method == 'GET':
        statExportTypes = StatExportType.objects.all()
        serializer = StatExportTypeSerializer(statExportTypes, many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=StatExportTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    
@api_view(['GET','PUT','DELETE'])
def statExportTypeDetail(request,statExportTypeId,format=None):
    
    try:
        statExportType = StatExportType.objects.get(statExportTypeId=statExportTypeId)
    except statExportType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StatExportTypeSerializer(statExportType)
        return Response(serializer.data)

    elif request.method =='PUT':
        serializer = StatExportTypeSerializer(statExportType,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        statExportType.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#PredictionType
@api_view(['GET','POST'])
def predictionTypeList(request, format=None):
    if request.method == 'GET':
        predictionTypes = PredictionType.objects.all()
        serializer = PredictionTypeSerializer(predictionTypes, many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=PredictionTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    
@api_view(['GET','PUT','DELETE'])
def predictionTypeDetail(request,predictionTypeId,format=None):
    
    try:
        predictionType = PredictionType.objects.get(predictionTypeId=predictionTypeId)
    except predictionType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PredictionTypeSerializer(predictionType)
        return Response(serializer.data)

    elif request.method =='PUT':
        serializer = PredictionTypeSerializer(predictionType,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        predictionType.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#University
@api_view(['GET','POST'])
def universityList(request, format=None):
    if request.method == 'GET':
        universities = University.objects.all()
        serializer = UniversitySerializer(universities, many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=UniversitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    
@api_view(['GET','PUT','DELETE'])
def universityDetail(request,universityId,format=None):
    
    try:
        university = University.objects.get(universityId=universityId)
    except university.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UniversitySerializer(university)
        return Response(serializer.data)

    elif request.method =='PUT':
        serializer = UniversitySerializer(university,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        university.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#University
@api_view(['GET','POST'])
def universityList(request, format=None):
    if request.method == 'GET':
        universities = University.objects.all()
        serializer = UniversitySerializer(universities, many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=UniversitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    
@api_view(['GET','PUT','DELETE'])
def universityDetail(request,universityId,format=None):
    
    try:
        university = University.objects.get(universityId=universityId)
    except university.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UniversitySerializer(university)
        return Response(serializer.data)

    elif request.method =='PUT':
        serializer = UniversitySerializer(university,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        university.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

