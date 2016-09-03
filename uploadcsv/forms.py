from django import forms

class UploadFileForm(forms.Form):
    namefile = forms.FileField(label="Cargar CSV con nombres")
