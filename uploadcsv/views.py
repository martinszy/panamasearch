from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core import files
from django.http import HttpResponseRedirect
from .forms import UploadFileForm

# Create your views here.

def index(request):
    return render(request, 'upload.html', {})

@csrf_exempt
def postcsv(request):
    #request.FILES.csvfile
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        handle_uploaded_file(request.FILES['namefile'])
        return render(request, 'upload.html', {'resultado': "Subida correcta"})
    else:
        redirect("/")

def handle_uploaded_file(f):
    with open('upload.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
