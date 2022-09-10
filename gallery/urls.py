from django.urls import path 
from . import views
from users import views as userviews

urlpatterns = [
    path("", views.gallery, name="gallery"),
    path('signup',userviews.signup, name="signup"),
    path('logout',userviews.logout,name='logout'),
    path('login',userviews.login,name="login"),
    
]

