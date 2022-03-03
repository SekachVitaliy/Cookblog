from django.urls import path
from .views import index, PostListView, PostDetailView

urlpatterns = [
    path('<slug:slug>', PostListView.as_view(), name='post_list'),
    path('<slug:slug>/<slug:post_slug>', PostDetailView.as_view(), name='post_single'),
    path('', index)
]
