from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post, Stream

@login_required
def index(request):
    user = request.user
    posts = Stream.objects.filter(user=user)
    group_ids = [post.post_id for post in posts]
    post_items = Post.objects.filter(id__in=group_ids).order_by('-posted')

    context = {'post_items': post_items}
    return render(request, 'index.html', context)



def post_detail(request, post_id):
    post = Post.objects.get(id = post_id)
    # user = user.request

    return render(request, 'post_detail.html', {'post':post})