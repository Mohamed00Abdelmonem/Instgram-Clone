from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import NewPostForm

@login_required
def index(request):
    user = request.user
    post_items = Post.objects.all().order_by('-posted')
    # posts = Stream.objects.filter(user=user)
    # group_ids = [post.post_id for post in posts]
    # post_items = Post.objects.filter(id__in=group_ids).order_by('-posted')

    context = {'post_items': post_items}
    return render(request, 'index.html', context)



def post_detail(request, post_id):
    post = Post.objects.get(id = post_id)
    # user = user.request

    return render(request, 'post_detail.html', {'post':post})




def new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.user = request.user
            my_form.save()
            return redirect('/')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {'form':form})    

