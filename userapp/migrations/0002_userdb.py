# Generated by Django 4.1.7 on 2023-04-11 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Email', models.EmailField(blank=True, max_length=30, null=True)),
                ('Number', models.IntegerField(blank=True, null=True)),
                ('Password', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
