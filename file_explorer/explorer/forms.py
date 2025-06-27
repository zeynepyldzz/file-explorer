from django import forms

class FileUploadForm(forms.Form):
    file = forms.FileField()

class FileEditForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)

class FolderCreateForm(forms.Form):
    folder_name = forms.CharField(max_length=255)

class MoveFileForm(forms.Form):
    destination_folder = forms.CharField(label='Destination Folder', max_length=255)


