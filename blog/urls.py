from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    path('create/', blog_create ,name='create'),
    path('detail/<int:id>', detail, name='detail'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>',delete, name='delete'),
    
]