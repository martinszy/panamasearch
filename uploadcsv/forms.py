from django import forms

class UploadFileForm(forms.Form):
    textlist = forms.CharField(max_length=50)
    namefile = forms.FileField()
