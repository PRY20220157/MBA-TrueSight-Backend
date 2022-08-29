# Generated by Django 4.1 on 2022-08-29 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "truesight",
            "0004_alter_loginattempt_userid_alter_prediction_userid_and_more",
        ),
        ("authapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="userTypeId",
            field=models.ForeignKey(
                db_column="user_type_id",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="truesight.usertype",
            ),
        ),
    ]