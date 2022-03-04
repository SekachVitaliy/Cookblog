from django.urls import path
from .views import PostListView, PostDetailView, HomeView

urlpatterns = [
    path('<slug:slug>/<slug:post_slug>/', PostDetailView.as_view(), name="post_single"),
    path('<slug:slug>/', PostListView.as_view(), name='post_list'),
    path('', HomeView.as_view(), name='home')
]
