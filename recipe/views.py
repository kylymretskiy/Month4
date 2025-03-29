from django.urls import reverse_lazy
from django.views import generic
from . import models , forms

class RecipeListView(generic.ListView):
    model = models.Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipe_list'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class RecipeDetailView(generic.DetailView):
    model = models.Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = self.object.ingredients.all()
        return context

class RecipeCreateView(generic.CreateView):
    model = models.Recipe
    form_class = forms.RecipeForm
    template_name = 'recipes/add_recipe.html'
    success_url = reverse_lazy('recipe_list')

class IngredientCreateView(generic.CreateView):
    model = models.Ingredient
    form_class = forms.IngredientForm
    template_name = 'recipes/add_ingredient.html'
    success_url = '/recipe_list/'

class RecipeDeleteView(generic.DeleteView):
    model = models.Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = '/recipe_list/'


