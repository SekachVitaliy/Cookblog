from django.forms import ModelForm
from .models import Post, Category, Recipe, Tag


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
