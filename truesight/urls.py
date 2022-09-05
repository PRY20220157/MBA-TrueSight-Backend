"""truesight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from truesight import views
from .views import *
from rest_framework import permissions
from rest_framework.urlpatterns import format_suffix_patterns
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title = "True Sight API",
        default_version = 'v1',
        description="An API for MBA success prediction",
    ),
    public= True,
    permission_classes=(permissions.AllowAny,),
    )

urlpatterns = [
    path("admin/", admin.site.urls),
    path('usertypes/<int:userTypeId>',views.userTypeDetail),
    path('countries/<int:countryId>',views.countryDetail),
    path('statexporttypes/<int:statExportTypeId>',views.statExportTypeDetail),
    path('predictiontypes/<int:predictionTypeId>',views.predictionTypeDetail),
    path('universities/<int:universityId>',views.universityDetail),
    path('predictions/<int:predictionId>',views.predictionDetail),
    path("usertypes/", views.userTypeList),
    path("countries/", views.countryList),
    path("statexporttypes/", views.statExportTypeList),
    path("predictiontypes/", views.predictionTypeList),
    path("universities/", views.universityList),
    path("predictions/", views.predictionList),
    path("users/",views.userList),
    path("userinfo/",views.userInfoList),
    path("model/train/", views.predictionTrain),
    path("model/singleprediction/", views.makePrediction),
    path("model/massiveprediction/",views.makeMassivePrediction),
    #swagger
    path('',schema_view.with_ui('swagger',cache_timeout=0),name="schema-swagger-ui"),
    #server time
    path('checkserver/',index,name='index'),
]

#urlpatterns = format_suffix_patterns(urlpatterns)