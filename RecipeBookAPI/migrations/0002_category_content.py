# Generated by Django 4.1.3 on 2022-11-21 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeBookAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]