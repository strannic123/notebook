from django.shortcuts import render, redirect
from .models import MyUser
from .forms import MyUserForm


def create_user(request):
    form = MyUserForm(request.POST or None)
    users = MyUser.objects.all()
    if form.is_valid():
        form.save()
        return redirect('/')
    template = 'index.html'
    context = {
        'form': form,
        'users': users
    }
    return render(request, template, context)


def update_user(request, id):
    id = MyUser.objects.get(id=id)
    form = MyUserForm(request.POST or None, instance=id)
    users = MyUser.objects.all()
    if form.is_valid():
        form.save()
        return redirect('/')
    template = 'index.html'
    context = {
        'form': form,
        'users': users
    }
    return render(request, template, context)


def delete_user(request, id):
    user = MyUser.objects.get(id=id)
    user.delete()

    return redirect('/')
