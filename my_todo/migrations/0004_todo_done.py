# Generated by Django 4.1.7 on 2023-04-02 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_todo', '0003_remove_user_phone_number_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
