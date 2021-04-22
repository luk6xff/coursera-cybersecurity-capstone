from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
from .models import Profile, Message
from .forms import LoginForm, UserRegistrationForm, \
                   UserEditForm, ProfileEditForm, \
                   CreateMessageForm


def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/")
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


@login_required
def send_message(request):
    form = CreateMessageForm()
    form.fields['receiver'] = forms.ModelChoiceField(queryset=User.objects.exclude(id=request.user.id))
    confirm = None
    if request.method == "POST":
        form = CreateMessageForm(request.POST)
        print("post")
        if form.is_valid():
            print(Profile)
            receiver = request.POST.get("receiver")
            #import pdb; pdb.set_trace()
            msg = Message.objects.create(
                receiver = Profile.objects.get(user=User.objects.get(id=receiver)),
                sender   = Profile.objects.get(user=User.objects.get(id=request.user.id)),
                message  = form.cleaned_data.get("message")
            )
            confirm = f"Message sent succesfully to: {User.objects.get(id=receiver).username}"
            msg.save()
        else:
            print("send_message form not valid!")
    context = {
        'msg_form' : form,
        'confirm' : confirm
    }
    return render(request, 'account/send_message.html', context)


@login_required
def inbox(request):
    context = {
        'msg_list' : Message.objects.all(),
    }
    return render(request, 'account/inbox.html', context)


@login_required
def dbdump(request):
    return render(request, 'db_dump.html', {})