# Generated by Django 5.1.7 on 2025-03-07 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='books/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('genre', models.CharField(choices=[('Ужасы', 'Ужасы'), ('Комедия', 'Комедия')], max_length=10)),
                ('time', models.TimeField()),
                ('director', models.CharField(max_length=100)),
            ],
        ),
    ]
