from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from result.forms import UserForm
from result.models import User


class HomeView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'result/home.html', {'form': form})

    def post(self, request):
        form = UserForm(data=request.POST)
        if not form.is_valid():
            return render(request, 'result/home.html', {'form': form})
        user_object = User.objects.get_or_create_user(name=request.POST['name'], email=request.POST['email'])
        if user_object:
            return render(request, 'result/subjects.html', {'id': user_object.id})
        else:
            return render(request, 'result/home.html', {'form': form})