# Generated by Django 5.0 on 2023-12-14 12:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_alter_user_action_choice_alter_user_password_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="action_choice",
            field=models.CharField(
                choices=[
                    ("admin", "admin"),
                    ("visitor", "visitor"),
                    ("creator", "creator"),
                ],
                default="visitor",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=2555),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=255),
        ),
    ]
