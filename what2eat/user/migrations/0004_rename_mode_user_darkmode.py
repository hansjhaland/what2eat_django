# Generated by Django 4.0.2 on 2022-03-16 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_mode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='mode',
            new_name='darkmode',
        ),
    ]
