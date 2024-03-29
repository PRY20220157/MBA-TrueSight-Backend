from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

class PredictionType(models.Model):

    predictionTypeId = models.AutoField(db_column='prediction_type_id',primary_key=True,unique=True)
    predictionType = models.CharField(db_column='prediction_type', max_length = 80)

    class Meta:
         db_table = 'prediction_type'

    def __str__(self):
        return str(self.predictionTypeId) +' - '+ self.predictionType

class StatExportType(models.Model):
    statExportTypeId = models.AutoField(db_column='stat_export_type_id',primary_key=True,unique=True)
    statExportType = models.CharField(db_column='stat_export_type', max_length = 80)

    class Meta:
        db_table = 'stat_export_type'

    def __str__(self):
        return str(self.statExportTypeId) +' - '+ self.statExportType

class Country(models.Model):
    countryId = models.AutoField(db_column='country_id',primary_key=True,unique=True)
    country = models.CharField(max_length=80)

    class Meta:
        db_table = 'country'

    def __str__(self):
        return str(self.countryId) +' - '+ self.country

class UserType(models.Model):
    userTypeId = models.AutoField(db_column='user_type_id',primary_key=True,unique=True)
    userType = models.CharField(db_column = 'user_type', max_length = 255)

    def __str__(self):
        return str(self.userTypeId) +' - '+ self.userType

    class Meta:
        db_table = 'user_type'

class University(models.Model):
    universityId = models.AutoField(db_column='university_id',primary_key=True,unique=True)
    university = models.CharField(max_length=80)
    university_email = models.CharField(max_length=120)
    countryId = models.ForeignKey(Country, default=138, on_delete=models.SET_NULL, null=True,db_column='country_id')

    class Meta:
        db_table = 'university'

    def __str__(self):
        return str(self.universityId) +' - '+ self.university

class UserAccountManager(BaseUserManager):
    def create_user(self,email,userTypeId,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        
        email = self.normalize_email(email)
        
        user = self.model(email=email,userTypeId=userTypeId)

        user.set_password(password)
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    userId = models.AutoField(db_column='user_id',primary_key=True,unique=True)
    userTypeId = models.ForeignKey(UserType, on_delete = models.SET_NULL, db_column = 'user_type_id', null=True)
    email = models.EmailField(max_length=255, unique=True, default='')
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['userTypeId']

    objects = UserAccountManager()

    class Meta:
        db_table = 'user'
         
    def __str__(self):
        return str(self.userId) +' - '+ self.email


class StatExport(models.Model):
    statExportId = models.AutoField(db_column='stat_export_id',primary_key=True,unique=True)
    statExportTypeId = models.ForeignKey(StatExportType, db_column = 'stat_export_type_id', on_delete=models.SET_NULL, null=True)
    userId = models.ForeignKey(User,null=True, blank=False, on_delete=models.SET_NULL, db_column='user_id')
    exportDate = models.DateTimeField(auto_now_add=True, db_column = 'export_date')

    class Meta:
        db_table = 'stat_export'

    def __str__(self):
        return str(self.statExportId) +' - '+ str(self.statExportTypeId) + ' ' + str(self.exportDate)

class UserInfo(models.Model):
    userInfoId = models.AutoField(db_column='user_info_id',primary_key=True,unique=True)
    countryId = models.ForeignKey(Country, on_delete=models.SET_NULL, db_column ='country_id',null=True)
    userId = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, db_column='user_id')
    universityId = models.ForeignKey(University, on_delete = models.SET_NULL, db_column = 'university_id',null=True)
    firstName = models.CharField(max_length = 255, db_column = 'first_name')
    lastName = models.CharField(max_length = 255, db_column = 'last_name')
    creationDate = models.DateTimeField(auto_now_add = True, db_column= 'creation_date')
    updatedDate = models.DateTimeField(auto_now_add=True, db_column='updated_date')

    class Meta:
        db_table = 'user_info'

    def __str__(self):
        return str(self.userInfoId) +' - '+ self.firstName +' '+ self.lastName
    

class LoginAttempt(models.Model):
    loginId = models.AutoField(db_column='login_id',primary_key=True,unique=True)
    userId = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, db_column='user_id')
    loginAttemptDate = models.DateTimeField(auto_now_add = True, db_column = 'login_attempt_date')
    isSuccesfull = models.BooleanField(db_column= 'is_successful', default=False)

    class Meta:
        db_table = 'login_attempt'

    def __str__(self):
        return str(self.loginId) +' - '+ self.userId +' '+ str(self.isSuccesfull)


class Prediction(models.Model):
    predictionId = models.AutoField(db_column='prediction_id',primary_key=True,unique=True)
    userId = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL, db_column='user_id')
    predictionTypeId = models.ForeignKey(PredictionType, null=True, blank=True, on_delete=models.SET_NULL, db_column = 'prediction_type_id')
    gmatScore = models.IntegerField(db_column = 'gmat_score', default=0)
    gpaScore = models.DecimalField(max_digits=3, decimal_places=2, db_column = 'gpa_score', default=0)
    workExp = models.IntegerField(db_column = 'work_exp', default=0)
    appType = models.IntegerField(db_column = 'app_type',default=0)
    gradGpaScore = models.DecimalField(max_digits=3, decimal_places=2, db_column = 'grad_gpa_score', default=0)
    creationDate = models.DateTimeField(auto_now_add = True, db_column= 'creation_date')
    massivePredictionId = models.IntegerField(null=True, blank=True, db_column = 'massive_prediction_id', default=None)
    studentId = models.CharField(max_length=255, db_column = 'student_id',default=None, blank=True, null=True)

    class Meta:
        db_table = 'prediction'

    def __str__(self):
        return str(self.predictionId) +' - '+str(self.userId) +' '+ str(self.creationDate)

class PredictionAverageValues(models.Model):
    predictionAverageValuesId = models.AutoField(db_column='prediction_average_values_id',primary_key=True,unique=True)
    gmatAvg = models.DecimalField(max_digits=5, decimal_places = 2, db_column='gmat_avg', default = 0)
    gpaAvg = models.DecimalField(max_digits=3, decimal_places = 2, db_column='gpa_avg', default = 0)
    gradGpaAvg = models.DecimalField(max_digits=3, decimal_places = 2, db_column='grad_gpa_avg', default = 0)
    workExpAvg = models.DecimalField(max_digits=5, decimal_places = 2, db_column='work_exp_avg', default = 0)
    appTypeAvg = models.IntegerField(db_column='app_type_avg', default=0)
    creationDate = models.DateTimeField(auto_now_add = True, db_column= 'creation_date')
    averageType = models.IntegerField(db_column='average_type', default=2)

    class Meta:
        db_table = 'prediction_average'

    def __str__(self):
        return str(self.predictionAverageValuesId) + ' - ' + str(self.creationDate)

class PredictionTraining(models.Model):
    predictionTrainingId = models.AutoField(db_column='prediction_training_id',primary_key=True,unique=True)
    predictionTypeId = models.ForeignKey(PredictionType, null=True, blank=True, on_delete=models.SET_NULL, db_column = 'prediction_type_id')
    gmatScore = models.IntegerField(db_column = 'gmat_score', default=0)
    gpaScore = models.DecimalField(max_digits=3, decimal_places=2, db_column = 'gpa_score', default=0)
    workExp = models.IntegerField(db_column = 'work_exp', default=0)
    appType = models.IntegerField(db_column = 'app_type',default=0)
    gradGpaScore = models.DecimalField(max_digits=3, decimal_places=2, db_column = 'grad_gpa_score', default=0)
    OaAtGrad = models.BooleanField(db_column = 'OA_at_grad', default=False)
    OaAt90 = models.BooleanField(db_column = 'OA_at_90', default=False)
    GradYear = models.IntegerField (db_column='grad_year')
    Salary = models.IntegerField(db_column='salary', default = 0)

    class Meta:
        db_table = 'prediction_training'

    def __str__(self):
        return str(self.predictionTrainingId) +' - '+str(self.predictionTypeId)
