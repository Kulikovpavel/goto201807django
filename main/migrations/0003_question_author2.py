# Generated by Django 2.0.7 on 2018-07-20 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_question_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author2',
            field=models.CharField(default='sdsd', max_length=200),
        ),
    ]
