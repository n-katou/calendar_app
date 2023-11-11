from django.shortcuts import render, redirect,get_object_or_404
from django.template import loader
from django.http import HttpResponse

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView,View
from django.urls import reverse_lazy,reverse

from .models import TodoModel
from .forms import TodoForm

from django.http import JsonResponse

from django.utils import timezone

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
    
class detail(DetailView):
    template_name = 'calendar_app/detail.html'
    model = TodoModel
    
class create(CreateView):
    template_name = 'calendar_app/create.html'
    model = TodoModel
    form_class = TodoForm
    success_url = reverse_lazy('cal:calendar')
    # リアルタイムを表示する方法
    # def get_initial(self):
    #     initial = super().get_initial()
    #     initial['start_date'] = timezone.now()
    #     initial['end_date'] = timezone.now()
    #     return initial

class delete(DeleteView):
    template_name = 'calendar_app/delete.html'
    model = TodoModel
    success_url = reverse_lazy('cal:calendar')
    
class update(UpdateView):
    template_name = 'calendar_app/update.html'
    model = TodoModel
    form_class = TodoForm
    # fields = ('title', 'memo', 'priority', 'start_date', 'end_date')
    success_url = reverse_lazy('cal:calendar')
    
    
def get_events(request):
    events = TodoModel.objects.all()
    event_data = []

    for event in events:
        event_data.append({
            'id': event.id,
            'title': event.title,
            'memo': event.memo,
            'start': event.start_date.isoformat(),
            'end': event.end_date.isoformat(),
            'status': event.priority,
        })

    return JsonResponse(event_data, safe=False)
