from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from MBATrueSight import *
import datetime as dt
import pandas as pd
import numpy as np
from datetime import datetime
from django.db.models import Q
import numbers

@api_view(['GET'])
def index(request):
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    message = 'server is live current time is '
    return Response(data=message + date, status = status.HTTP_200_OK)

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





#Prediction
@api_view(['GET','POST'])
def predictionList(request, format=None):
    if request.method == 'GET':
        predictions = Prediction.objects.all()
        serializer = PredictionSerializer(predictions, many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=PredictionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    
@api_view(['GET','PUT','DELETE'])
def predictionDetail(request,predictionId,format=None):
    
    try:
        prediction = Prediction.objects.get(predictionId=predictionId)
    except prediction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PredictionSerializer(prediction)
        return Response(serializer.data)

    elif request.method =='PUT':
        serializer = PredictionSerializer(prediction,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        prediction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#User
@api_view(['GET','POST'])
def userList(request, format=None):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    if request.method=='POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

#User by email
@api_view(['POST'])
def getUserByEmail(request, format=None):
    try:
        email = request.data['email']
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    users = User.objects.filter(email=email)

    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

#UserInfo by email
@api_view(['POST'])
def getUserByEmail(request, format=None):
    try:
        email = request.data['email']
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    users = User.objects.filter(email=email)
    serializer = UserSerializer(users, many=True)
    
    finalResponse = []
    userdict, userinfodict = {},{}
    userdict['user']=serializer.data
    
    finalResponse.append(userdict)

    for user in serializer.data:
        try:
            userId = user['userId']
            userInfos = UserInfo.objects.filter(userId=userId)
            uiSerializer = UserInfoSerializer(userInfos,many=True)
            userinfodict['userInfo']=uiSerializer.data
            finalResponse.append(userinfodict)

        except:            
            response = {"Response":"No userinfo exists with this email {email}"}
            finalResponse.append(response)

    return Response(finalResponse)

#User Info PUT
@api_view(['PUT'])
def editUserInfo(request, userId, format=None):

    try:
        userInfo = UserInfo.objects.get(userId=userId)
    except userInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =='PUT':
        serializer = UserInfoSerializer(userInfo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Prediction  
@api_view(['GET','PUT','DELETE'])
def predictionDetail(request,predictionId,format=None):
    
    try:
        prediction = Prediction.objects.get(predictionId=predictionId)
    except prediction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PredictionSerializer(prediction)
        return Response(serializer.data)

    elif request.method =='PUT':
        serializer = PredictionSerializer(prediction,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        prediction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#UserInfo
@api_view(['GET','POST'])
def userInfoList(request, format=None):
    if request.method == 'GET':
        userInfos = UserInfo.objects.all()
        serializer = UserInfoSerializer(userInfos, many=True)
        return Response(serializer.data)

    if request.method=='POST':
        serializer=UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)



#-------------------------------
#Models
@api_view(['GET'])
def predictionTrain(request,format=None):
    try: 
        run_training()
        return Response(status=status.HTTP_200_OK)
    except:
        return Reponse(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def makePrediction(request,format=None):

    predictions = []
    
    for entry in request.data:
        try:
            userId = entry.pop('userId')
        except:
            userId = None
        print("Entry:",entry)
        result = RFpredict(entry)
        predictions.append(result)

    try:
        request.data[0]['userId']=userId
    except:
        print(type(request.data[0]))

    try:    
        request.data[0]['predictionTypeId']=1 #simple
    except:
        print(type(request.data[0]))


    try:
        request.data[0]['gmatScore']=request.data[0].pop('gmat')
        request.data[0]['gpaScore']=request.data[0].pop('gpa')
        request.data[0]['workExp']=request.data[0].pop('wk_xp')
        request.data[0]['appType']=request.data[0].pop('app_type')
        request.data[0]['gradGpaScore']=round(predictions[0][0],2)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer = PredictionSerializer(data=request.data[0])
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def makeMassivePrediction(request,format=None):
    
    input_file = request.FILES['file']
    try:
        df = pd.read_csv(input_file)
    except:
         try:
            df = pd.read_excel(input_file)
         except:
             response = Response(status=status.HTTP_400_BAD_REQUEST)
             return response

    df = df.reset_index()

    finalPredictions = []
    for index, row in df.iterrows():
        predictionArray = []
        singlePredictionDict ={}

        try:
            gmat = float(row['gmat'])
            gpa = float(row['gpa'])
            wk_xp = float(row['wk_xp'])
            app_type = float(row['app_type'])
        except:
            continue
        
        predictionArray.extend((gmat,gpa,wk_xp,app_type))

        result = RFpredict(predictionArray)

        singlePredictionDict = {
            "gmat":gmat,
            "gpa":gpa,
            "wk_xp":wk_xp,
            "app_type":app_type,
            "grad_gpa":result[0]
        }

        finalPredictions.append(singlePredictionDict)

    response = Response()
    response.data=finalPredictions

    print(finalPredictions)

    try:
        massivePredictionId = request.data['massive_prediction_id']
    except:
        try:
            massivePredictionId =  Prediction.objects.filter(~Q(massivePredictionId=None)).last().massivePredictionId
            if isinstance(massivePredictionId,numbers.Number):
                massivePredictionId = massivePredictionId + 1
            else:
                massivePredictionId = 1
        except:
            response = Response(status=status.HTTP_400_BAD_REQUEST)
            return response


    userId = int(request.data['user_id'])
    predictionTypeId = 2

    count=0
    for pred in finalPredictions:
        count=count+1
        print(count)
        try:
            pred['gmatScore']=pred.pop('gmat')
            pred['gpaScore']=pred.pop('gpa')
            pred['workExp']=pred.pop('wk_xp')
            pred['appType']=pred.pop('app_type')
            pred['gradGpaScore']=round(pred.pop('grad_gpa'),2)
            pred['userId']=userId
            pred['predictionTypeId']=predictionTypeId
            pred['massivePredictionId']=massivePredictionId
            serializer = PredictionSerializer(data=pred)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except:
            continue

    return (response)


@api_view(['POST'])
def predictionsByUserId(request, format=None):
    if request.method == 'POST':
        try:
            userId = request.data['userId']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        predictions = Prediction.objects.filter(userId=userId)

        serializer = PredictionSerializer(predictions, many=True)
        return Response(serializer.data)

@api_view(['DELETE'])
def deletePredictionsByUserId(request,userId, format=None):
    
    try:
        predictions = Prediction.objects.filter(userId=userId)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    print(predictions)
    predictions.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def deletePredictionsByMassivePredictionId(request,massivePredictionId,format=None):
    
    try:
        predictions = Prediction.objects.filter(massivePredictionId=massivePredictionId)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    predictions.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def deletePredictionsByMassivePredictionIdAndUserId(request,massivePredictionId,userId,format=None):
    
    try:
        predictions = Prediction.objects.filter(massivePredictionId=massivePredictionId, userId=userId)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    predictions.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def getPredictionsByDate(request, format=None):
    try:   
        userId = request.data['userId']
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        startDate = request.data['startDate']
        endDate = request.data['endDate']
    except:
        startDate = '01/01/1995'
        endDate = '12/31/2050'
    try:
        smonth, sday, syear = startDate.split("/",2)
        emonth, eday, eyear = endDate.split("/",2)
        smonth, sday, syear = int(smonth), int(sday), int(syear)
        emonth, eday, eyear = int(emonth), int(eday), int(eyear)
    except:
        startDate = '01/01/1995'
        endDate = '12/31/2050'
        smonth, sday, syear = startDate.split("/",2)
        emonth, eday, eyear = endDate.split("/",2)
        smonth, sday, syear = int(smonth), int(sday), int(syear)
        emonth, eday, eyear = int(emonth), int(eday), int(eyear)
    
    predictions = Prediction.objects.filter(creationDate__gte=dt.date(syear, smonth, sday),
                                        creationDate__lte=dt.date(eyear, emonth, eday),
                                        userId=userId)

    serializer = PredictionSerializer(predictions, many=True)
    return Response(serializer.data)



