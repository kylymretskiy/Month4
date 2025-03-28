from django import forms
from . import models, parser_janmates

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('janmates.com', 'janmates.com'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]
    def parser_data(self):
        if self.data['media_type'] == 'janmates.com':
            janmates_films = parser_janmates.parsing_janmates()
            for i in janmates_films:
                models.JanmatesBooksModel.objects.create(**i)