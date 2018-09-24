# users/views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import CustomUserCreationForm


class UserFormView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

'''
class UserFormView(View):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit = False)
            #cleaned data
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(email = email, password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #request.user.email
                    return redirect('home')

        return render(request, self.template_name, {'form' : form})
'''

            

