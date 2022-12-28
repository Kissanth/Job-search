# Generated by Django 4.1.4 on 2022-12-25 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postingmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=25)),
                ('Experience', models.IntegerField()),
                ('Email', models.EmailField(default='exampel@hotmail.in', max_length=254)),
            ],
        ),
    ]
