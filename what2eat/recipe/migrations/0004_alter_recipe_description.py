# Generated by Django 4.0.2 on 2022-03-23 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_recipe_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
