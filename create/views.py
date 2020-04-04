from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from .create_pdf import create_pdf as cp
import os

STATIC_URL = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static\\')

def pdf_view(path):
    if os.path.exists(path):
        with open(path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(path)
            return response
    raise Http404

def create_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.created_date = timezone.now()
            user.save()
            certificate = cp(user.name, user.university_roll, user.certificate)
            path = cp.create(certificate)
            path = os.path.join(STATIC_URL, os.path.join('Kriraathon Certificates', path))
            if os.path.exists(path):
                with open(path, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type="application/pdf")
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(path)
                    return response
            raise Http404
            #pdf_view(path)
            #response = HttpResponse(content_type='application/force-download') # mimetype is replaced by content_type for django 1.7
            #response['Content-Disposition'] = 'attachment; filename=certificate.pdf'
            #response['X-Sendfile'] = path
            #return response

    else:
        form = UserForm()
    return render(request, 'create/create_new.html', {'form': form})

def download(request, pk):
    obj = User.objects.get(pk=pk)
    return render(request, 'create/download.html', {'user': obj})