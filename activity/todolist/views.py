from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
from django.views.generic import CreateView


# Create your views here.
def HomeView(request):
    dataset = Post.objects.all()
    context = {'dataset':dataset}
    return render(request,'home.html',context)

class AddPostView(CreateView):
     model = Post
     form_class = PostForm
     template_name = 'addpost.html'  
       

# def CreatePost(request):
#     form  = PostForm(request.POST)

#     if request.method == 'POST':
#         form  = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         else:
#             form = PostForm()    

#     return render(request, 'addpost.html' , {'form': form})
        


