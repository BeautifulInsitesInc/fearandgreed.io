# Generated by Django 3.2 on 2021-05-27 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tital_tag',
            field=models.CharField(default='Article', max_length=255),
        ),
    ]