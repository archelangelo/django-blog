"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post'),
    path('poster/', views.CreatePostView.as_view(), name='poster'),
    path('post/<int:pk>/edit', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post_delete'),
    path('drafts/', views.DraftListView.as_view(), name='draft_list'),
    path('post/<int:pk>/comment', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve', views.approve_comment, name='approve_comment'),
    path('comment/<int:pk>/delete', views.delete_comment, name='delete_comment'),
    path('post/<int:pk>/publish', views.post_publish, name='post_publish'),
]