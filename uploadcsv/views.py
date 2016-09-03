from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from uploadcsv.models import Namelist, NamelistForm

# Create your views here.

def index(request):
    model = Namelist;
    namelists = Namelist.objects.all();

    if request.method == 'POST':
        form = NamelistForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Namelist(namefile=request.FILES['namefile'])
            instance.status = "Pending"
            instance.save()
            return render(request, 'index.html', {'form': form, 'resultado': "El archivo ha sido subido corectamente."})
        else:
            return render(request, 'index.html', {'form': form,'resultado': "Ha ocurido un error, el archivo no pudo ser subido."})
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})

def cola(request):
    model = Namelist;
    namelists = Namelist.objects.all();
    return render(request, 'cola.html', {'namelists': namelists})
