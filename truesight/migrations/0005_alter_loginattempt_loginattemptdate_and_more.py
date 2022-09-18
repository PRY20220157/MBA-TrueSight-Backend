# Generated by Django 4.1 on 2022-09-09 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truesight', '0004_prediction_apptype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginattempt',
            name='loginAttemptDate',
            field=models.DateTimeField(auto_now_add=True, db_column='login_attempt_date'),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='creationDate',
            field=models.DateTimeField(auto_now_add=True, db_column='creation_date'),
        ),
        migrations.AlterField(
            model_name='statexport',
            name='exportDate',
            field=models.DateTimeField(auto_now_add=True, db_column='export_date'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='creationDate',
            field=models.DateTimeField(auto_now_add=True, db_column='creation_date'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='updatedDate',
            field=models.DateTimeField(auto_now_add=True, db_column='updated_date'),
        ),
    ]