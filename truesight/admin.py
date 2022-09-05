from django.contrib import admin
from .models import *

admin.site.register(Country)
admin.site.register(UserType)
admin.site.register(StatExportType)
admin.site.register(PredictionType)
admin.site.register(University)
admin.site.register(UserInfo)
admin.site.register(Prediction)