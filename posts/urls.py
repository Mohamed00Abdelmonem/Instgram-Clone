from django.urls import path
from .views import index, post_detail, new_post


urlpatterns = [

    path('',index, name='index'),
    # path('post<int:post_id>', post_detail, name="post_detail")
    path('post/<uuid:post_id>/', post_detail, name='post_detail'),
    path('new_post', new_post, name="new_post")


]