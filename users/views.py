from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import auth  
from django.http.response import HttpResponseRedirect  
from django.urls import reverse_lazy  
from django.views.generic import FormView, UpdateView
from django.contrib.auth import login, authenticate  
from users.forms import ProfileCreationForm  
from users.models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.socialaccount.models import SocialAccount


class RegisterView(FormView):  
  
    form_class = UserCreationForm  
  
    def form_valid(self, form):  
        form.save()  
        username = form.cleaned_data.get('username')  
        raw_password = form.cleaned_data.get('password1')  
        login(self.request, authenticate(username=username, password=raw_password))  
        return super(RegisterView, self).form_valid(form)  
  
  
class CreateUserProfile(FormView):  
  
    form_class = ProfileCreationForm  
    template_name = 'profile-create.html'  
    success_url = reverse_lazy('main')  
  
    def dispatch(self, request, *args, **kwargs):  
        if self.request.user.is_anonymous:  
            return HttpResponseRedirect(reverse_lazy('users:login'))  
        return super(CreateUserProfile, self).dispatch(request, *args, **kwargs)  
  
    def form_valid(self, form):  
        instance = form.save(commit=False)  
        instance.user = self.request.user  
        instance.save()  
        return super(CreateUserProfile, self).form_valid(form)


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'profile_form.html'
    model = UserProfile
    fields = ['age']

    success_url = reverse_lazy('main')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        super(ProfileUpdate, self).form_valid(form)
        social = SocialAccount.objects.filter(provider='github', user=self.request.user).first()
        if social:
            social.extra_data['age'] = form.instance.age
            social.save()
        return HttpResponseRedirect(self.get_success_url())