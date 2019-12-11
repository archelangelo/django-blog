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
import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about', views.AboutViews.as_view(), 'about'),
    path('post/<int:pk>', views.PostDetailView.as_view(), 'post'),
    path('poster/', views.CreatePostView.as_view(), 'poster'),
    path('post/<int:pk>/edit', views.PostUpdateView.as_view(), 'post_edit'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), 'post_delete'),
    path('drafts/', views.DraftListView.as_view(), 'draft_list'),
]