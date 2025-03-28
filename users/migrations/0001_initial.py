# Generated by Django 5.1.7 on 2025-03-28 10:13

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('degree', models.CharField(choices=[('bachelor', 'Бакалавр'), ('master', 'Магистр'), ('docent', 'Доцент'), ('none', 'Без диплома')], default='none', max_length=20)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10)),
                ('age', models.PositiveIntegerField(default=7)),
                ('phone_number', models.CharField(max_length=20)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('salary', models.PositiveIntegerField(blank=True, null=True)),
                ('experience', models.PositiveIntegerField(default=0)),
                ('skills', models.TextField(blank=True)),
                ('languages', models.CharField(blank=True, max_length=200)),
                ('address', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
