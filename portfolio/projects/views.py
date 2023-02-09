from django.shortcuts import render, get_object_or_404
from .models import Job, PostImage


def homepage(request):
    jobs = Job.objects.all()
    return render(request, 'index.html', {'jobs': jobs})


def detail(request, job_id):
    post = get_object_or_404(Job, pk=job_id)
    photos = PostImage.objects.filter(post=post)

    return render(request, 'detail.html', {'post': post,
                                           'photos': photos})
