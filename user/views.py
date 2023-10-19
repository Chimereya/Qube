from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from .forms import CreateUserForm, UpdateUserForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout  # login
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required



# Create your views here.


@unauthenticated_user
def register_page(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, ' Account was created for ' + user)
            return redirect('user:login')
        else:
            messages.info(request, "Invalid username or password.")

    return render(request, 'user/signup.html', {'form': form})


@unauthenticated_user
def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('core:home')
            else:
                messages.info(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request=request, template_name="user/login.html", context={"form": form})


def logout_page(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('core:home')


def user_profile(request, pk):
    user = User.objects.get(id=pk)
    return render(request, 'user/profile.html', {'user': user})


def edit_profile(request, pk):
    user = User.objects.get(id=pk)
    if request.method == "POST":
        u_form = UpdateUserForm(request.POST, request.FILES, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "your account has been updated successfully!")
            return redirect('user:profile', pk)
    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'user/update_profile.html', {'user': user, 'u_form': u_form,
                                                        'p_form': p_form})


