# Generated by Django 4.0.2 on 2022-02-15 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_alter_recipe_publisheddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='publishedDate',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
    ]