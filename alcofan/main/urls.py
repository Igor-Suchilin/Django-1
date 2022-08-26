from django.urls import path
from . import views
from .views import show_post, show_category


urlpatterns = [
    path('', views.index, name='home'),
    path('base/', views.base, name='base'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category')
]