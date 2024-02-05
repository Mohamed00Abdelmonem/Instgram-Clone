from django.urls import path
from .views import signup, activate, profile

app_name = 'accounts'

urlpatterns= [
    path('signup', signup, name='signup'),
    path('<str:username>/activate', activate),
    path('profile', profile, name='profile_user'),
    # path('dashboard', dashboard),
    # path('edituser', update_user, name='edit_profile'),

]


