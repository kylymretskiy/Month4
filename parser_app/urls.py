from django.urls import path
from . import views

urlpatterns = [
    path("janmates_list/", views.JanmatesBooksListView.as_view(), name="janmates_list"),
    path("parser_form/", views.ParserForm.as_view(), name="parser_form"),
]