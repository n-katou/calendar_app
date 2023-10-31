from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import TodoModel

#ログイン機能
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required #ログイン機能

def calendar(request):
    todolists = TodoModel.objects.all()
    context = {
        'todolists': todolists,
    }
    
    # template = loader.get_template("calendar_app/calendar.html")
    # return HttpResponse(template.render())
    return render(request, 'calendar_app/calendar.html', context)


class list(ListView):
    template_name = "calendar_app/list.html"
    model = TodoModel
    context_object_name = 'items'
    
class detail(DetailView):
    template_name = 'calendar_app/detail.html'
    model = TodoModel
    
class create(CreateView):
    template_name = 'calendar_app/create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('cal:calendar')

class delete(DeleteView):
    template_name = 'calendar_app/delete.html'
    model = TodoModel
    success_url = reverse_lazy('cal:calendar')
    
class update(UpdateView):
    template_name = 'calendar_app/update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('cal:calendar')
    
    