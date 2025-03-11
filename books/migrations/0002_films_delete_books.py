# Generated by Django 5.1.7 on 2025-03-11 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='books/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('genre', models.CharField(choices=[('Ужасы', 'Ужасы'), ('Комедия', 'Комедия')], max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('director', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='books',
        ),
    ]
