"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from p_library import views
from p_library.views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many, FriendEdit, FriendList
from users.views import ProfileUpdate


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.books_list, name='main'),
    path('publish/', views.publish),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('author/create/', AuthorEdit.as_view(), name='author_create'),
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('author/create_many/', author_create_many, name='author_create_many'),
    path('author_book/create_many/', books_authors_create_many, name='author_book_create_many'),
    path('friend/create/', FriendEdit.as_view(), name='friend_create'),
    path('friends/', FriendList.as_view(), name='friend_list'),
    path('', include('users.urls', namespace='users')),
    path('', include('p_library.urls', namespace='p_library')),
    path('accounts/', include('allauth.urls')),
    path('userprofile/', ProfileUpdate.as_view(), name='userprofile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)