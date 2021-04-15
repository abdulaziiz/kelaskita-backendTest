from django.shortcuts import render
from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView

from .models import Post

def home(request):
    data = Post.objects.all()
    count_hit = True
    return render(request, "index.html",{"posts":data})
