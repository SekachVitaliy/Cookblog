from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import PostForm, CategoryForm, RecipeForm, TagForm
from .models import Post


class HomeView(ListView):
    model = Post
    paginate_by = 9
    template_name = "blog/home.html"


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'


class CategoryAddView(CreateView):
    form_class = CategoryForm
    template_name = 'blog/add_category.html'
    success_url = reverse_lazy('home')


class RecipeAddView(CreateView):
    form_class = RecipeForm
    template_name = 'blog/add_recipe.html'
    success_url = reverse_lazy('home')


class TagAddView(CreateView):
    form_class = TagForm
    template_name = 'blog/add_tag.html'
    success_url = reverse_lazy('home')


def add_post(request):
    form = PostForm()
    context = {'form': form}
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('home'))
    return render(request, 'blog/add_post.html', context)
