from django.urls import path
from p_library import views
from p_library.views import books_list


app_name = 'p_library'


urlpatterns = [  
     path('books_list/', views.books_list, name='books_list'),
]