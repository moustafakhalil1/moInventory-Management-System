
from django.urls import path,include
from . import views
urlpatterns = [
   path('register/',views.register,name='register'),
   path('profile/',views.profile,name='profile'),
   path('profile/profile_update',views.profile_update,name='profile-update'),
   path('profile/user_updates',views.user_update,name='user-update'),
   path('profile/settings',views.setting,name='user-setting'),
    
]
