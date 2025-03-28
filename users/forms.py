from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


DEGREE_CHOICES = (
        ("bachelor", "Бакалавр"),
        ("master", "Магистр"),
        ("docent", "Доцент"),
        ("none", "Без диплома"),
    )

GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

class CustomRegisterForm(UserCreationForm):
    degree = forms.ChoiceField(choices=DEGREE_CHOICES, required=True, label="Укажите диплом")
    gender = forms.ChoiceField(choices=GENDER, required=True, label='Укажите пол')
    age = forms.IntegerField(required=True, label='Укажите возраст')
    phone_number = forms.CharField(required=True, label='Укажите номер')
    email = forms.EmailField(required=True, label="укажите EMAIL")
    experience = forms.IntegerField(required=True, label="Укажите опыт работы")
    skills = forms.CharField(widget=forms.Textarea, required=False, label="Укажите навыки")
    languages = forms.CharField(required=False, label="Укажите языки")
    address = forms.CharField(required=True, label="Укажите адрес")


    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'gender',
            'phone_number',
            'degree',
            'experience',
            'skills',
            'languages',
            'address',
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.degree = self.cleaned_data['degree']
        user.gender = self.cleaned_data['gender']
        user.age = self.cleaned_data['age']
        user.phone_number = self.cleaned_data['phone_number']
        user.email = self.cleaned_data['email']
        user.experience = self.cleaned_data['experience']
        user.skills = self.cleaned_data['skills']
        user.languages = self.cleaned_data['languages']
        user.address = self.cleaned_data['address']

        if commit:
            user.save()
        return user