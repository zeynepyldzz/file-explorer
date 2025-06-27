

from django.http import HttpResponse
from .models import File
from .forms import FileUploadForm, FileEditForm

import os
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import FileUploadForm, FolderCreateForm

def list_files_in_folder(request, folder):
    folder_path = os.path.join('/', folder)
    files = os.listdir(folder_path)
    file_upload_form = FileUploadForm()
    folder_create_form = FolderCreateForm()
    return render(request, 'explorer/list_files_in_folder.html', {'folder': folder, 'files': files, 'file_upload_form': file_upload_form, 'folder_create_form': folder_create_form})

def upload_file(request, folder):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_name = request.FILES['file'].name
            file_path = os.path.join('/', folder, file_name)
            with open(file_path, 'wb') as destination:
                for chunk in request.FILES['file'].chunks():
                    destination.write(chunk)
            return JsonResponse({'success': True, 'message': 'File uploaded successfully.'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid form submission.'})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


def create_folder(request):
    if request.method == 'POST':
        folder_name = request.POST.get('folder_name')

        # Burada klasör oluşturma işlemini gerçekleştirin

        return JsonResponse({'success': True, 'message': 'Folder created successfully.'})

    return render(request, 'explorer/create_folder.html')

def copy_file(request, file_id):
    try:
        # Hedef dosyanın File modeli üzerinden bulunması
        source_file = File.objects.get(id=file_id)

        # Dosyayı kopyala
        destination_file = File(name=f"Copy_of_{source_file.name}", content=source_file.content)
        destination_file.save()

        # Dosya kopyalandıktan sonra list_files view fonksiyonuna yönlendirme yapılıyor.
        return redirect('list_files')

    except File.DoesNotExist:
        return HttpResponse("Source file does not exist.", status=404)

    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=500)



def move_file(request, file_id, destination_folder):
    try:
        # Hedef dosyanın File modeli üzerinden bulunması
        source_file = File.objects.get(id=file_id)

        # Hedef klasör yolu oluşturuluyor
        destination_path = os.path.join('/', destination_folder)

        # Dosyayı taşı
        source_file.content.name = os.path.join(destination_path, source_file.name)
        source_file.save()

        # Dosya taşındıktan sonra list_files view fonksiyonuna yönlendirme yapılıyor.
        return redirect('list_files')

    except File.DoesNotExist:
        return HttpResponse("Source file does not exist.", status=404)

    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=500)





def list_files(request):
    # Local diskteki tüm klasörleri bul
    root_path = '/'
    folders = [f for f in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, f))]

    # Tüm dosyaları ve klasörleri al
    files = File.objects.all()

    return render(request, 'explorer/list_files.html', {'files': files, 'folders': folders})

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            File.objects.create(name=file.name, type=file.content_type, content=file.read())
            return redirect('list_files')
    else:
        form = FileUploadForm()
    return render(request, 'explorer/upload_file.html', {'form': form})

def download_file(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    response = HttpResponse(file.content, content_type=file.type)
    response['Content-Disposition'] = f'attachment; filename="{file.name}"'
    return response

def delete_file(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    file.delete()
    return redirect('list_files')

def edit_file(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    if request.method == 'POST':
        form = FileEditForm(request.POST)
        if form.is_valid():
            file.content = form.cleaned_data['content']
            file.save()
            return redirect('list_files')
    else:
        form = FileEditForm(initial={'content': file.content})
    return render(request, 'explorer/edit_file.html', {'form': form, 'file': file})


