from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy,reverse
from .forms import PostForm 
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
# def home(request):

#     return render(request,'home.html', {})


def LikeView(request, pk):
    post = get_object_or_404(Post, id=pk)

    # Ajouter ou retirer le like
    if request.user in post.likes.all():
        post.likes.remove(request.user)  # Retire le like si déjà liké
        liked = False
    else:
        post.likes.add(request.user)  # Ajoute le like
        liked = True

    # Retourner le statut et le nombre de likes
    return JsonResponse({
        'liked': liked,
        'likes_count': post.likes.count()
    })
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'objects_list'  # Utiliser 'objects_list' dans le template
    ordering = ['-post_date']  # Décommenter si tu souhaites ordonner les posts par ID descendant


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context['total_likes'] = total_likes
        return context

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm
    # fields = '__all__'
    success_url = reverse_lazy('home')


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag','body']
    success_url = reverse_lazy('home')    

class DeletePostView(DeleteView):
    model = Post
    # form_class = PostForm
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home') 

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Assigne l'utilisateur actuel comme auteur
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})


def instaView(request):
    posts = Post.objects.all()  # Remplacez 'Post' par le nom de votre modèle
    return render(request, 'instagram.html', {'object_list': posts})



@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        # Si l'utilisateur a déjà "liké", retire le "like"
        post.likes.remove(request.user)
    else:
        # Sinon, ajoute le "like"
        post.likes.add(request.user)
    return redirect('article-detail', pk=pk)