
#url configuration in the app

from django.urls import path
from . import views
urlpatterns = [
     #'' mean homepage
     path('', views.PostList.as_view(), name='home'),
     # slug here mean continue from previous url through slug generating url method
     path('<slug:slug>/', views.post_detail, name='post_detail'),
     #mean other pages beside home page, new-page
     #reference:https://djangocentral.com/creating-comments-system-with-django/
     path('/',views.about_us,name='about_us'),
]
