from django.contrib import admin
from .models import *
from authapp.models import User as AUser

admin.site.register(Country)
admin.site.register(UserType)
admin.site.register(StatExportType)
admin.site.register(PredictionType)
admin.site.register(University)
admin.site.register(UserInfo)
admin.site.register(Prediction)
admin.site.register(AUser)