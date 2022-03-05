from django.urls import path
from .views import PostListView, PostDetailView, HomeView, add_post, CategoryAddView, RecipeAddView, TagAddView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('add_tag/', TagAddView.as_view(), name='add_tag'),
    path('add_post/', add_post, name='add_post'),
    path('add_recipe/', RecipeAddView.as_view(), name='add_recipe'),
    path('add_category/', CategoryAddView.as_view(), name='add_category'),

    path('<slug:slug>/<slug:post_slug>/', PostDetailView.as_view(), name="post_single"),
    path('<slug:slug>/', PostListView.as_view(), name='post_list'),
]
