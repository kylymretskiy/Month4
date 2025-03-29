from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:id>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/add/', views.RecipeCreateView.as_view(), name='add_recipe'),
    path('ingredient/add/', views.IngredientCreateView.as_view(), name='add_ingredient'),
    path('recipe/<int:id>/delete/', views.RecipeDeleteView.as_view(), name='delete_recipe'),
]

