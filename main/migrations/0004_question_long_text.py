# Generated by Django 2.0.7 on 2018-07-21 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_question_author2'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='long_text',
            field=models.TextField(default=''),
        ),
    ]
