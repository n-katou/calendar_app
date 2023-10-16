# from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

#ログイン機能
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required #ログイン機能

def calendar(request):
    """
    カレンダー画面
    """
    template = loader.get_template("calendar_app/calendar.html")
    return HttpResponse(template.render())
