from django.contrib.auth.views import LoginView, LogoutView
from users.views import RegisterView, CreateUserProfile
from django.urls import path, reverse_lazy
from allauth.account.views import login, logout


app_name = 'users'


urlpatterns = [  
	path('login/', login, name='login'),  
	path('logout/', logout, name='logout'),
	path('register/', RegisterView.as_view(
        template_name='register.html',
		success_url=reverse_lazy('users:profile-create')
    	), name='register'),
  	path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),
	  
]